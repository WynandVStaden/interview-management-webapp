from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from notes.models import Note
from .models import Candidate
from .forms import CandidateForm


def candidate_search(request):
    # Retrieve the search query from the GET parameters
    search_query = request.GET.get('search_query', '')

    # Perform the search using the candidate name
    candidates = Candidate.objects.filter(name__icontains=search_query)

    # You can add additional logic or filtering based on your requirements

    context = {
        'candidates': candidates,
        'search_query': search_query,
    }

    return render(request, 'candidates/candidate_search.html', context)


def home(request):
    return render(request, 'home.html')


def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates/candidate_list.html', {'candidates': candidates})


def candidate_detail(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    notes = Note.objects.filter(candidate_id=candidate.id)
    return render(request, 'candidates/candidate_detail.html',
                  {'candidate': candidate, 'notes': notes, 'candidate_id': candidate.id})


def candidate_create(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save()
            Note.objects.create(
                candidate=candidate,
                title="INTERVIEWS",
                content=''
            )
            Note.objects.create(
                candidate=candidate,
                title="ASSESSMENTS",
                content=''
            )
            return redirect('candidate_list')
    else:
        form = CandidateForm()
    return render(request, 'candidates/candidate_form.html', {'form': form})


def candidate_edit(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('candidate_detail', pk=pk)
    else:
        form = CandidateForm(instance=candidate)
    return render(request, 'candidates/candidate_form.html', {'form': form})


def candidate_delete(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)

    if request.method == 'POST':
        candidate.delete()
        messages.success(request, 'Candidate deleted successfully.')

    return redirect('candidate_list')


def candidate_notes(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    # Add logic to retrieve and display candidate's notes
    return render(request, 'candidates/candidate_notes.html', {'candidate': candidate})
