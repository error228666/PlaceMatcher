from django.contrib import admin
from .models import Places, Category, Metro, Review



admin.site.register(Metro)
admin.site.register(Places)
admin.site.register(Review)
admin.site.register(Category)