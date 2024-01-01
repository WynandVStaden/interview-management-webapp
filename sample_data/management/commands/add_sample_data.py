# sample_data/management/commands/add_sample_data.py
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management.base import BaseCommand
from candidates.models import Candidate
from notes.models import Note
from django.contrib.auth.models import User
from django.core.files import File


class Command(BaseCommand):
    help = 'Add sample data to the database'

    def handle(self, *args, **kwargs):
        # Ensure there's at least one user
        if not User.objects.exists():
            self.stdout.write(self.style.ERROR('No users found. Please create a user first.'))
            return

        # Add sample candidates
        user = User.objects.first()
        for i in range(5):
            candidate = Candidate.objects.create(
                name=f'candidate {i}',
                email=f'email{i}@gmail.com',
                cell_phone=f'0{i}12345678',
                resume='resumes/simple_pdf.pdf'
            )
            # Add two notes for each candidate
            for j in range(2):
                s_title = ""
                if j == 0:
                    s_title = "INTERVIEWS"
                else:
                    s_title = "ASSESSMENTS"
                Note.objects.create(
                    candidate=candidate,
                    title=s_title,
                    content=s_title + ' content'
                )
        self.stdout.write(self.style.SUCCESS('Sample candidates added successfully.'))
