from django.urls import path
from .views import (candidate_list,
                    candidate_detail, candidate_create,
                    candidate_edit, candidate_delete, candidate_notes, candidate_search)

urlpatterns = [
    path('candidates/', candidate_list, name='candidate_list'),
    path('candidates/<int:pk>/', candidate_detail, name='candidate_detail'),
    path('candidates/create/', candidate_create, name='candidate_create'),
    path('candidates/<int:pk>/edit/', candidate_edit, name='candidate_edit'),
    path('candidates/<int:candidate_id>/delete/', candidate_delete, name='candidate_delete'),
    path('candidates/<int:candidate_id>/notes/', candidate_notes, name='candidate_notes'),
    path('candidate_search/', candidate_search, name='candidate_search'),
]
