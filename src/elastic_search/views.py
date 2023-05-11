import abc
# import pdb; pdb.set_trace()
from django.shortcuts import render, redirect
from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

from core.models import Places, Category, Metro, Review
from core.documents import PlacesDocument, UserDocument
from core.serializers import UserSerializer, PlacesSerializer
from elasticsearch import Elasticsearch

import operator
from functools import reduce

"""
class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()
            qs = search.to_queryset()

            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')
            for hit in response.hits:
                print(hit.name)
            print(response)
           

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)



            context = {
                'queryset': qs,
                'categories': Category.objects.all(),

                'metro': Metro.objects.all()
            }
            return render(request, "mainpage/search.html", context)
           # return self.get_paginated_response(serializer.data)
        



        except Exception as e:
            return HttpResponse(e, status=500)
        


        
# views


class SearchUsers(PaginatedElasticSearchAPIView):
    serializer_class = UserSerializer
    document_class = UserDocument

    def generate_q_expression(self, query):
        return Q('bool',
                 should=[
                     Q('match', username=query),
                     Q('match', first_name=query),
                     Q('match', last_name=query),
                 ], minimum_should_match=1)


class SearchPlacesgg(PaginatedElasticSearchAPIView):
    serializer_class = PlacesSerializer
    document_class = PlacesDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'name',
                    'adress',
                    'metro.name',
                    'category.name'
                ], fuzziness='auto')

"""

from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView


class SearchPlaces(APIView, LimitOffsetPagination):
    serializer = PlacesSerializer
    search_document = PlacesDocument

    def get(self, request, query=None):
        try:
            finalquery = []
            q = request.GET.get('search', None)
            name_contains = request.GET.get('name_contains', None)
            person_count = request.GET.get('person_count', None)
            min_rating = request.GET.get('min_rating', None)
            category = request.GET.get('category', None)
            metro = request.GET.get('metro', None)
            price = request.GET.get('price', None)
            
            if name_contains is not None and not name_contains == '':
                finalquery.append(Q(
                    'multi_match',
                    query=name_contains,
                    fields=[
                        'name',
                        'adress',
                    ],
                    fuzziness='auto'))
                
                
            if category is not None and not category == '':
                finalquery.append(Q(
                    'multi_match',
                    query=category,
                    fields=[
                        'category__name',
                    ],
                    fuzziness='auto'))
     
            if metro is not None and not metro == '':
                finalquery.append(Q(
                    'bool',
                    must=[
                        Q('match', metro__name=metro),
                    ],
                    fuzziness='auto'))    
                
                
            if len(finalquery) > 0:
                search = self.search_document.search().query(reduce(operator.iand, finalquery))                
                response = search.execute()
                qs = search.to_queryset()


            # q = Q(
            #     "multi_match",
            #     query=query,
            #     fields=['name',
            #         'adress',
            #         'metro.name',
            #         'category.name'],
            #     fuzziness="auto",
            # ) & Q(
            #     should=[
            #         Q("match", is_default=True),
            #     ],
            #     minimum_should_match=1,
            # )

            search = self.search_document.search().query(q)
            response = search.execute()
            qs = search.to_queryset()

            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')
            for hit in response.hits:
                print(hit.name)


            context = {
                'queryset': qs,
                'categories': Category.objects.all(),

                'metro': Metro.objects.all()
            }
            return render(request, "mainpage/search.html", context)
#            results = self.paginate_queryset(response, request, view=self)
#           serializer = self.serializer(results, many=True)
#            return self.get_paginated_response(serializer.data)

        except Exception as e:
            return HttpResponse(e, status=500)



def ElasticSearchView(request):
    try:
    #    es = elasticsearch.Elasticsearch(hosts=[ES_HOST], )
    #    idx_list = es.cat.indices(index='foobar-20*', h='index', s='index:desc').split()
    #    q = Q("match_all")
        search = PlacesDocument.search().query(Q("match_all"))
        response = search.execute()
        qs = search.to_queryset()


        serializer = PlacesSerializer
        search_document = PlacesDocument
        finalquery = []
        q = request.GET.get('search', None)
        name_contains = request.GET.get('name_contains', None)
        person_count = request.GET.get('person_count', None)
        min_rating = request.GET.get('min_rating', None)
        category = request.GET.get('category', None)
        metro = request.GET.get('metro', None)
        price = request.GET.get('price', None)
        
        if name_contains is not None and not name_contains == '':
            finalquery.append(Q(
                'multi_match',
                query=name_contains,
                fields=[
                    'name',
                    'adress',
                ],
                fuzziness='auto'))
            
            
        if category is not None and not category == '' and not category == 'Выбрать...':
            finalquery.append(Q(
                'multi_match',
                query=category,
                fields=[
                    'category',
                ]))
    
        if metro is not None and not metro == '' and not metro == 'Выбрать...':
            finalquery.append(Q(
                'bool',
                must=[
                    Q('match_phrase', metro__name=metro),
                ]))    
            
            
        if len(finalquery) > 0:
            q = reduce(operator.iand, finalquery)
            print(q)
            search = search_document.search().query(reduce(operator.iand, finalquery))                
            response = search.execute()
            qs = search.to_queryset()
            print(f'Found {response.hits.total.value} hit(s) for query: "{finalquery}"')
            for hit in response.hits:
                print(hit.name)


        # q = Q(
        #     "multi_match",
        #     query=query,
        #     fields=['name',
        #         'adress',
        #         'metro.name',
        #         'category.name'],
        #     fuzziness="auto",
        # ) & Q(
        #     should=[
        #         Q("match", is_default=True),
        #     ],
        #     minimum_should_match=1,
        # )

        # search = search_document.search().query(q)
        # response = search.execute()
        # qs = search.to_queryset()




        context = {
            'queryset': qs,
            'categories': Category.objects.all(),

            'metro': Metro.objects.all()
        }
        return render(request, "mainpage/search.html", context)
#            results = self.paginate_queryset(response, request, view=self)
#           serializer = self.serializer(results, many=True)
#            return self.get_paginated_response(serializer.data)

    except Exception as e:
        return HttpResponse(e, status=500)

