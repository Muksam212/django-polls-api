from django.urls import path
from ..views.vote import (
    VoteCreateAPIView,
    VoteListAPIView
)
urlpatterns = [
    path('api/vote/create/', VoteCreateAPIView.as_view(), name = 'api-vote-create'),
    path('api/vote/list/', VoteListAPIView.as_view(), name = 'api-vote-list')
]
