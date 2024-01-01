from django.db import models
from candidates.models import Candidate


class Note(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=255, null=True)
    content = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return f"Note for {self.candidate.name}"
