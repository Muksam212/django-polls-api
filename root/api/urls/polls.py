from ..views.polls import (
    PollList,
    PollDetails,
    PollSpecific
)
from django.urls import path

urlpatterns = [
    path('api/poll/list/', PollList.as_view(), name = 'api-poll-list'),
    path('api/poll/<int:id>/', PollDetails.as_view(), name = 'api-poll-details'),
    path('api/poll/user/specific/', PollSpecific.as_view(), name = 'api-poll-specific')
]
