from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from .views import SearchView

urlpatterns = [
    path('', SearchView, name="search")
    ]

