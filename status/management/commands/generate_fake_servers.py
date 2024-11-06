from django.core.management.base import BaseCommand
from faker import Faker
import random
from status.models import Server

class Command(BaseCommand):
    help = 'Generate fake server data'

    def handle(self, *args, **kwargs):
        Server.objects.all().delete()
        fake = Faker()
        statuses = ['up', 'down']
        severities = ['low', 'medium', 'high']

        # Generate 20 fake servers
        for _ in range(20):
            name = fake.domain_word() + "_server"  # Generates a fake server name
            status = random.choice(statuses)  # Randomly choose between 'up' or 'down'

            if status == 'up': 
                severity = 'N/A'

            if status == 'down':
                severity = random.choice(severities)  # Randomly choose a severity level
            Server.objects.create(name=name, status=status, severity=severity)

        self.stdout.write(self.style.SUCCESS('Successfully generated fake server data!'))
