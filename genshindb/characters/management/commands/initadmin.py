from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create default superuser'

    def handle(self, *args, **options):
        User.objects.create_superuser('admin', 'admin@example.com', 'pass')
        