from rest_framework import serializers
from polls.models import Poll

from ..serializers.choice import ChoiceSerializer

class PollSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    choices = ChoiceSerializer(many = True)
    class Meta:
        model = Poll
        fields = ("id","question", "created_by", "pub_date", "choices")