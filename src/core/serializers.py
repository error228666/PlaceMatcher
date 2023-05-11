from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MetroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metro
        fields = '__all__'



class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = "mainpage.Profile"
        fields = '__all__'


class PlacesSerializer(serializers.ModelSerializer):
    metro = MetroSerializer(many=True)
    category = CategorySerializer(many=True)
    favourites = FavouritesSerializer(many=True)

    class Meta:
        model = Places
        fields = '__all__'