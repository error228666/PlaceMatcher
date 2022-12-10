from django.contrib import admin
from .models import Places, Category, Metro


admin.site.register(Metro)
admin.site.register(Places)

admin.site.register(Category)