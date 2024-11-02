from ..serializers.choice import ChoiceSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from polls.models import Choice
from rest_framework.permissions import IsAuthenticated
from .filters import ChoiceFilter
from django_filters.rest_framework import DjangoFilterBackend

class ChoiceList(ListCreateAPIView):
    serializer_class = ChoiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ChoiceFilter
    model = Choice
    queryset = Choice.objects.all()

class ChoiceDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = ChoiceSerializer
    model = Choice
    queryset = Choice.objects.all()
    lookup_field = "id"



class ChoiceUserList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChoiceSerializer
    model = Choice

    def get_queryset(self):
        response = self.model.objects.filter(poll__created_by = self.request.user)
        return response