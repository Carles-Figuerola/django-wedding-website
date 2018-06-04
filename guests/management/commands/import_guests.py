from django.core.management import BaseCommand
from guests import csv_import


class Command(BaseCommand):
    filename = 'guests-file.csv'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path'] 
        csv_import.import_guests(path)
