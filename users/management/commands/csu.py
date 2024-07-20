from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='draignair@gmail.com',
            nick_name='admin',
            country='Russia',
            is_staff=True,
            is_superuser=True,
        )
        user.set_password('admin')
        user.save()
