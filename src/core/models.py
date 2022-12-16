from django.db import models
from mainpage.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Metro(models.Model):
    name = models.CharField(max_length=30,blank=True, null=True)
    line = models.IntegerField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class Places(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    metro = models.ManyToManyField(Metro)
    category = models.ManyToManyField(Category)
    adress = models.CharField(max_length=180, blank=True, null=True)
    site = models.CharField(max_length=270, blank=True, null=True)
    vk = models.CharField(max_length=45, blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    min_count_of_people = models.IntegerField(blank=True, null=True)
    max_count_of_people = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    favourites = models.ManyToManyField(Profile)

    def __str__(self):
        return self.name

class Review(models.Model):
    place = models.ManyToManyField(Places)
    min = models.IntegerField(blank=True, null=True)
    max = models.IntegerField(blank=True, null=True)
    text = models.TextField()
    user = models.ManyToManyField(Profile)
    rating = models.FloatField(null=True)
    date = models.DateField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)