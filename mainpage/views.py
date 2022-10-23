from django.shortcuts import render
from django.http import HttpResponse


def mainpage(request):
    return render(request, "mainpage/mainpage.html")


def friends(request):
    return render(request, "mainpage/friends.html")


def search(request):
    return render(request, "mainpage/search.html")


def favorites(request):
    return render(request, "mainpage/favorites.html")


def meetings(request):
    return render(request, "mainpage/meetings.html")


def profile(request):
    return render(request, "mainpage/profile.html")


def login(request):
    return render(request, "mainpage/login.html")


