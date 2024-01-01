from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def all_notes(request):
    notes = Note.objects.all()
    return render(request, 'notes/all_notes.html', {'notes': notes})


def note_list(request, candidate_id):
    notes = Note.objects.filter(candidate_id=candidate_id)
    return render(request, 'notes/note_list.html', {'notes': notes, 'candidate_id': candidate_id})


def note_detail(request, note_id, candidate_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/note_detail.html', {'note': note, 'candidate_id': candidate_id})


def note_create(request, candidate_id):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.candidate_id = candidate_id
            note.save()
            return redirect('note_detail', note_id=note.id)
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'candidate_id': candidate_id})


def note_edit(request, note_id, candidate_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', note_id=note_id, candidate_id=candidate_id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'note': note})


def note_delete(request, note_id, candidate_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully.')

    return redirect('candidate_detail', pk=candidate_id)
