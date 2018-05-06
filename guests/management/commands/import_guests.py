from django.core.management import BaseCommand
from guests import csv_import


class Command(BaseCommand):
    filename = 'guests-file.csv'

    def handle(self, *args, **kwargs):
        csv_import.import_guests('/home/carles/src/django-wedding-website/guests-test.csv')
