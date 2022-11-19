from django.core.management.base import BaseCommand
from core.models import Places, Category
import csv


def add_data(row):
    place = Places(name=row[0], adress=row[3], site=row[20], vk=row[24])
    place.save()
    categories = row[2].split(";")
    for cat in categories:
        category = Category.objects.get_or_create(name=cat)
        place.category.add(Category.objects.get(name=cat))
    place.save()


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
                    if count > 15:
                        break
                    count+=1
                    add_data(row)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
