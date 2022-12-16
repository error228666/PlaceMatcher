from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from .views import SearchView, PlaceView, Vk, Website, ReviewView, ThanksView, FavAdd

urlpatterns = [
    path('', SearchView, name="search"),
    path('<int:placeid>', PlaceView, name="place"),
    path('<int:placeid>/vk', Vk, name="vk"),
    path('<int:placeid>/website', Website, name="website"),
    path('<int:placeid>/review', ReviewView, name="review"),
    path('<int:placeid>/thanks', ThanksView, name="thanks"),
    path('fav<int:placeid>', FavAdd, name="favadd")

]

