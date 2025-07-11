from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from accounts.models import User, Profile
from task.models import Task

from django.utils import timezone


class Command(BaseCommand):
    help = 'create objects for tester or frontend developer'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.faker = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.faker.email(), password=self.faker.password())
        profile = Profile.objects.get(user=user)
        for i in range(10):
            Task.objects.create(
                owner=user,
                title=self.faker.word(),
                description=self.faker.text(),
                created_at=timezone.now(),
            )
