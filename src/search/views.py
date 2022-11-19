from django.shortcuts import render
from core.models import Places, Category

def is_valid_queryparam(param):
    return param != '' and param is not None


def SearchView(request):
    qs = Places.objects.all()

    name_contains = request.GET.get('name_contains')
    person_count = request.GET.get('person_count')
    min_rating = request.GET.get('min_rating')
    category = request.GET.get('category')
    show_results = 0

    if (is_valid_queryparam(name_contains) or is_valid_queryparam(person_count)
        or is_valid_queryparam(min_rating) or is_valid_queryparam(category) ):
        show_results = 1
    if is_valid_queryparam(name_contains):
        qs = qs.filter(name__icontains=name_contains)
    if is_valid_queryparam(min_rating):
        qs = qs.filter(average_rating__gte=min_rating)
    if is_valid_queryparam(person_count):
        qs = qs.filter(min_count_of_people__lte=name_contains)
        qs = qs.filter(max_count_of_people__gte=name_contains)
    if is_valid_queryparam(category) and category != "Choose...":
        qs = qs.filter(category__name=category)
    context = {
        'queryset': qs,
        'categories': Category.objects.all(),
        'show' :show_results
    }
    return render(request, "mainpage/search.html", context)