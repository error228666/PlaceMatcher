from django.shortcuts import render


def SearchView(request):
    return render(request, "mainpage/search.html")