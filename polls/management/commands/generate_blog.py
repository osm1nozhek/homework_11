import random

from django.core.management.base import BaseCommand
from faker import Faker
from polls.models import Blog

fake = Faker()


class Command(BaseCommand):
    help = "Generate blog"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count", type=int, default=100, help="Number of blog to generate"
        )

    def handle(self, *args, **options):
        count = options["count"]
        for i in range(count):
            title = fake.sentence(nb_words=7, variable_nb_words=False)
            content=fake.text(max_nb_chars=500)
            Blog.objects.create(title=title, content=content)
        self.stdout.write(
            self.style.SUCCESS(f"Successfully generated {count} teachers.")
        )