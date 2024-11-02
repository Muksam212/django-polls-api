from .users import urlpatterns as users_urlpatterns
from .polls import urlpatterns as polls_urlpatterns
from .choice import  urlpatterns as choice_urlpatterns
from .vote import urlpatterns as vote_urlpatterns


from django.urls import path, include

urlpatterns = [
    path('', include(users_urlpatterns)),
    path('', include(polls_urlpatterns)),
    path('', include(choice_urlpatterns)),
    path('', include(vote_urlpatterns))
]
