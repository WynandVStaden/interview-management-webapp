from django.urls import path
from .views import note_list, note_detail, note_create, note_edit, all_notes, note_delete

urlpatterns = [
    path('notes/<int:candidate_id>/', note_list, name='note_list'),
    path('notes/view_note/<int:note_id>/<int:candidate_id>', note_detail, name='note_detail'),
    path('notes/<int:candidate_id>/create/', note_create, name='note_create'),
    path('notes/<int:note_id>/<int:candidate_id>/edit/', note_edit, name='note_edit'),
    path('notes/all_notes', all_notes, name='all_notes'),
    path('note/<int:note_id>/<int:candidate_id>/delete/', note_delete, name='note_delete'),
]
