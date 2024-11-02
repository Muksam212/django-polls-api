from rest_framework import serializers
from polls.models import *


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ("choice", "poll", "voted_by")