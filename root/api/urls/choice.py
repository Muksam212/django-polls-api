from ..views.choice import (
    ChoiceList,
    ChoiceDetails,
    ChoiceUserList
)
from django.urls import path

urlpatterns = [
    path('api/choice/list/', ChoiceList.as_view(), name = 'api-choice-list'),
    path('api/choice/details/<int:id>/', ChoiceDetails.as_view(), name = 'api-choice-details'),
    path('api/choice/user/list/', ChoiceUserList.as_view(), name = 'api-choice-user-list')
]
