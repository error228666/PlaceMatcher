from django.core.management.base import BaseCommand
from core.models import Places, Category, Metro
import csv
import math
import geopy
from geopy.geocoders import Nominatim
import geopy.distance
from time import sleep


def add_place(row):
    place = Places(name=row[0], adress=row[3], site=row[20], vk=row[24])
    place.save()
    categories = row[2].split(";")
    for cat in categories:
        category = Category.objects.get_or_create(name=cat)
        place.category.add(Category.objects.get(name=cat))
    place.save()
#     try:
#         metro = find_nearest_metro(place)
#         place.metro.add(Metro.objects.get(name=metro))
#     except AttributeError:
#         pass
#
# def convert_coordinates(coord):
#     degree = math.floor(coord)
#     minutes = math.floor((coord - degree) * 100)
#     seconds = ((coord-degree)*100 - minutes) * 100
#     res = degree + minutes / 60 + seconds / 3600
#     return res
#
#
# def find_nearest_metro(place):
#     address = "Санкт-Петербург, " + place.adress
#     index = address.find(" лит ")
#     if index != -1:
#         address = address[:index]
#     geopy.geocoders.options.default_user_agent = "myapp"
#     geolocator = Nominatim()
#     location = geolocator.geocode(address)
#     width = location.latitude
#     longitude = location.longitude
#     metros = Metro.objects.all()
#     min = 0
#
#     for metro in metros:
#         if min == 0:
#             min = geopy.distance.geodesic((metro.width, metro.longitude), (width, longitude))
#             res = metro.name
#         else:
#             if (min > geopy.distance.geodesic((metro.width, metro.longitude), (width, longitude))):
#                 min = geopy.distance.geodesic((metro.width, metro.longitude), (width, longitude))
#                 res = metro.name
#     return res
#
#


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_places', type=str)
        # parser.add_argument('file_metro', type=str)

    def handle(self, *args, **kwargs):
        file_places = kwargs['file_places']
        # file_metro = kwargs['file_metro']

        # with open(f'{file_metro}.csv', encoding='utf-8') as r_file:
        #     file_reader = csv.reader(r_file, delimiter=",")
        #     count = 0
        #     for row in file_reader:
        #         if count == 0:
        #             count = 1
        #         else:
        #             w = convert_coordinates(float(row[2]))
        #             l = convert_coordinates(float(row[3]))
        #             metro = Metro(line=row[0], name=row[1], width=w, longitude=l)
        #             metro.save()

        with open(f'{file_places}.csv', encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = 0
            for row in file_reader:
                count1 = 0
                if count == 0:
                    count = 1

                else:
                    if count > 50:
                        break
                    count+=1
                    count1+=1
                    add_place(row)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
