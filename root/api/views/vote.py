from ..serializers.vote import VoteSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from polls.models import Vote

class VoteCreateAPIView(CreateAPIView):
    serializer_class = VoteSerializer

    def post(self, request, format = None):
        serializer = VoteSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg":"success"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"error":"Failed"}, status = status.HTTP_404_NOT_FOUND)
        

class VoteListAPIView(ListAPIView):
    serializer_class = VoteSerializer
    model = Vote
    queryset = Vote.objects.all()