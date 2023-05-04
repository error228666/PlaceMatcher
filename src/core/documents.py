
from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from core.models import Places, Category, Metro, Review
from elasticsearch_dsl import analyzer, tokenizer


autocomplete_analyzer = analyzer('autocomplete_analyzer',
            tokenizer=tokenizer('trigram', 'nGram', min_gram=1, max_gram=20),
            filter=['lowercase']
        )

@registry.register_document
class UserDocument(Document):
    class Index:
        name = 'users'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
        ]



@registry.register_document
class PlacesDocument(Document):

    # name = fields.TextField(
    #     attr='name',
    #     fields={
    #         'suggest': fields.Completion(),
    #     }
    # )

    name = fields.TextField(analyzer='russian', search_analyzer='russian') 


    
#     category = fields.ObjectField(properties={
#         'name': fields.TextField(analyzer='russian', search_analyzer='russian'),
#   #      analyzer: 'russian',
#     })
    category = fields.TextField(                                    
        attr='category_indexing',                                     
        analyzer='russian',                                     
        fields={                                         
            'raw': fields.KeywordField(multi=True),                                         
#            'suggest': fields.CompletionField(multi=True),                                      
        },                                     
        multi=True                                 
    )

    metro = fields.ObjectField(properties={
        'name': fields.TextField(analyzer='russian', search_analyzer='russian'),
    #    analyzer: 'russian',
    })


    class Index:
        name = 'places'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Places
        fields = [
          #  'name',
            'adress',
            'average_rating',
            'min_count_of_people',
            'max_count_of_people',
            'price',

        ]
