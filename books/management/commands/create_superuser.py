from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    """
    Creates superuser if not exists.
    """

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username=os.environ.get('SUPERUSER_USER'),
                email=os.environ.get('SUPERUSER_EMAIL'),
                password=os.environ.get('SUPERUSER_PASSWORD')
            )
            self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser already exists"))