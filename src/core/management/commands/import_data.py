from django.core.management.base import BaseCommand
from core.models import Places, Category
import csv
import math


def add_place(row):
    place = Places(name=row[0], adress=row[3], site=row[20], vk=row[24])
    place.save()
    categories = row[2].split(";")
    for cat in categories:
        category = Category.objects.get_or_create(name=cat)
        place.category.add(Category.objects.get(name=cat))
    place.save()
    #metro = find_nearest_metro(place)
    #place.metro.add(Metro.objects.get(name=metro))




"""def find_nearest_metro(place):
    adress = "Санкт-Петербург, " + place.adress
    print(adress)
    geopy.geocoders.options.default_user_agent = "myapp"
    geolocator = Nominatim()
    location = geolocator.geocode(adress)
    width = location.latitude
    longitude = location.latitude
    metros = Metro.objects.all()
    min = 0

    for metro in metros:
        if min == 0:
            min = geopy.distance.geodesic((width, metro.width), (longitude, metro.longitude))
            res = metro.name
        else:
            if (min > geopy.distance.geodesic((width, metro.width), (longitude, metro.longitude))):
                min = geopy.distance.geodesic((width, metro.width), (longitude, metro.longitude))
                res = metro.name
    return res"""




class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_places', type=str)
        #parser.add_argument('file_metro', type=str)

    def handle(self, *args, **kwargs):
        file_places = kwargs['file_places']
        #file_metro = kwargs['file_metro']

        """with open(f'{file_metro}.csv', encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            for row in file_reader:
                if count == 0:
                    count = 1
                else:
                    metro = Metro(line=row[0], name=row[1], width=row[2], longitude=row[3])
                    metro.save()"""

        with open(f'{file_places}.csv', encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            for row in file_reader:
                if count == 0:
                    count = 1
                else:
                    if count > 15:
                        break
                    count+=1
                    add_place(row)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
