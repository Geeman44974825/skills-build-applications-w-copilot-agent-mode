from django.core.management.base import BaseCommand
from octofit_app.models import *  # Import your models here

class Command(BaseCommand):
    help = 'Populates the database with initial data for development or testing.'

    def handle(self, *args, **options):
        # Example: Create a user (customize as needed)
        # User.objects.create(username='testuser', email='test@example.com')
        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
