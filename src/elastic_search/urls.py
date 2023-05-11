
from django.urls import path

from elastic_search.views import SearchPlaces, ElasticSearchView

urlpatterns = [
#    path('', SearchPlaces.as_view(), name="search"),
    path('', ElasticSearchView, name="e_search"),
#    path('user/<str:query>/', SearchUsers.as_view()),
 #   path('<str:query>/', SearchPlaces.as_view()),
]