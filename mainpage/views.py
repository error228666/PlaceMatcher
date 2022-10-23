from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView


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

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


