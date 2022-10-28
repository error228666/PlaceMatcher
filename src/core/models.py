from django.db import models

class Places(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=270, blank=True, null=True)
    adress = models.CharField(max_length=180, blank=True, null=True)
    site = models.CharField(max_length=270, blank=True, null=True)
    vk = models.CharField(max_length=45, blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    min_count_of_people = models.IntegerField(blank=True, null=True)
    max_count_of_people = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    other_info = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'places'

class Type(models.Model):
    name = models.CharField(max_length=270, blank=True, null=True)

    def __str__(self):
        return self.name