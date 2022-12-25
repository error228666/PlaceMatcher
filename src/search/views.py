from django.shortcuts import render, redirect
from core.models import Places, Category, Metro, Review
from mainpage.models import Profile
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def is_valid_queryparam(param):
    return param != '' and param is not None


def SearchView(request):

    qs = Places.objects.all()

    name_contains = request.GET.get('name_contains')
    person_count = request.GET.get('person_count')
    min_rating = request.GET.get('min_rating')
    category = request.GET.get('category')
    metro = request.GET.get('metro')
    price = request.GET.get('price')


    if is_valid_queryparam(name_contains):
        qs = qs.filter(name__icontains=name_contains)

    if is_valid_queryparam(price):
        qs = qs.filter(Q(price__lte=price) | Q(price=None))

    if is_valid_queryparam(min_rating):
        qs = qs.filter(Q(average_rating=None) | Q(average_rating__gte=min_rating))

    if is_valid_queryparam(person_count):
        qs = qs.filter(Q(min_count_of_people__lte=person_count) | Q(min_count_of_people=None))
        qs = qs.filter(Q(max_count_of_people__gte=person_count) | Q(min_count_of_people=None))

    if is_valid_queryparam(category) and category != "Выбрать...":
        qs = qs.filter(category__name=category)

    if is_valid_queryparam(metro) and metro != "Выбрать...":
        qs = qs.filter(metro__name=metro)

    context = {
        'queryset': qs,
        'categories': Category.objects.all(),

        'metro': Metro.objects.all()
    }
    return render(request, "mainpage/search.html", context)


def PlaceView(request, placeid):

    place = Places.objects.get(id=placeid)
    review = Review.objects.all()
    review = review.filter(place=place)
    is_logged = 0
    text = ""
    if (request.user.id):
        if place.favourites.filter(id=request.user.id).exists():
            text = "Удалить из избранного"
        else:
            text = "Добавить в избранное"
        is_logged = 1
    context = {
        'review': review,
        'text': text,
        'login': is_logged,
        'place': Places.objects.get(id=placeid)
    }
    return render(request, "mainpage/place.html", context)

def Vk(request, placeid):
    return redirect(f"{Places.objects.get(id=placeid).vk}")
def Website(request, placeid):
    return redirect(f"{Places.objects.get(id=placeid).site}")

@login_required
def ReviewView(request, placeid):
    profile = Profile.objects.get(id=request.user.id)
    place = Places.objects.get(id=placeid)
    review = Review.objects.all()
    review = review.filter(user=profile)
    review = review.filter(place=place)
    review_abbility = 0
    if len(review) == 0:
        review_abbility = 1
    context = {
        'abil' : review_abbility,
        'place': place
    }
    return render(request, "mainpage/review.html", context)

def UpdatePlace(place, min, max, rating, price):
    reviews = Review.objects.all()
    reviews = reviews.filter(place=place)
    if is_valid_queryparam(min):
        if place.min_count_of_people is None:
            place.min_count_of_people = min
            place.save()
        else:
            i = 0
            sum = 0
            for r in reviews:
                if r.min is not None:
                    sum += r.min
                    i += 1
            place.min_count_of_people = round(sum / i)
            place.save()


    if is_valid_queryparam(max):
        if place.max_count_of_people is None:
            place.max_count_of_people = max
            place.save()
        else:
            i = 0
            sum = 0
            for r in reviews:
                if r.max is not None:
                    sum += r.max
                    i += 1
            place.max_count_of_people = round(sum / i)
            place.save()

    if place.average_rating is None:
        place.average_rating = rating
        place.save()
    else:
        i = 0
        sum = 0
        for r in reviews:
            if r.rating is not None:
                sum += r.rating
                i += 1
        place.average_rating = round(sum / i)
        place.save()

    if place.price is None:
        place.price = price
        place.save()
    else:
        i = 0
        sum = 0
        for r in reviews:
            if r.price is not None:
                sum += r.price
                i += 1
        place.average_rating = round(sum / i)
        place.save()


def ThanksView(request, placeid):
    place = Places.objects.get(id=placeid)
    user = Profile.objects.get(id=request.user.id)
    message = request.POST.get('message')
    min_person_count = request.POST.get('min')
    max_person_count = request.POST.get('max')
    print(max_person_count)
    print(min_person_count)
    if is_valid_queryparam(min_person_count) and is_valid_queryparam(max_person_count) is not None and min_person_count > max_person_count:
        context = {'text': "Максимальное количество не может быть меньше минимального", 'button': 1, 'place': place}
        return render(request, "mainpage/thanks.html", context)
    rating = request.POST.get('rating')
    if is_valid_queryparam(rating) == 0:
        context = {'text': "Введите вашу оценку", 'button': 1,'place': place}
        return render(request, "mainpage/thanks.html", context)
    price = request.POST.get('price')
    review = Review(text=message, rating=rating)
    if is_valid_queryparam(min_person_count):
        review.min = min_person_count
    if is_valid_queryparam(max_person_count):
        review.max = max_person_count
    if is_valid_queryparam(price):
        review.price = price
    review.save()
    review.place.add(place)
    review.user.add(user)
    review.save()

    UpdatePlace(place, min_person_count, max_person_count, rating, price)

    context = {'text': "Спасибо за ваш отзыв!", 'button': 0, 'place': place}
    return render(request, "mainpage/thanks.html", context)

@login_required
def FavAdd(request, placeid):
    user = Profile.objects.get(id=request.user.id)
    place = Places.objects.get(id=placeid)
    if place.favourites.filter(id=request.user.id).exists():
        place.favourites.remove(user)
    else:
        place.favourites.add(user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])