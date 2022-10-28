from django.core.management.base import BaseCommand
from core.models import Places, Type
from django.core.exceptions import MultipleObjectsReturned
from django.db.utils import DataError
import csv


def add_data(row):
    type = Type.objects.get_or_create(name=row[2])
    place = Places.objects.get_or_create(name=row[0], type=row[2], adress=row[3], site=row[20], vk=row[24])

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']

        with open(f'{file_name}.csv', encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            for row in file_reader:
                if count == 0:
                    count = 1
                else:
                    try:
                        add_data(row)
                    except (MultipleObjectsReturned, DataError):
                        pass

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
