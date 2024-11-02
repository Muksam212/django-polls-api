from rest_framework import serializers
from polls.models import *


class ChoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Choice
        fields = ("id","poll", "choice_text")