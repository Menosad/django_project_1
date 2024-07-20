from django.contrib.auth.models import Group
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        group = Group.objects.create(name='модераторы')
        group.save()
