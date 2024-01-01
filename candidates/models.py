from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    cell_phone = models.CharField(max_length=15, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

