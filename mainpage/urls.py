from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.mainpage, name="home"),
    path("search/", views.search, name="search"),
    path("profile/", views.profile, name="profile"),
    path("friends/", views.friends, name="friends"),
    path("favorites/", views.favorites, name="favorites"),
    path("meetings/", views.meetings, name="meetings"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("signup/", views.SignUp.as_view(), name="signup"),
]