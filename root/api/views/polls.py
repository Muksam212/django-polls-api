from ..serializers.polls import PollSerializer
from polls.models import Poll

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

class PollList(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many = True)
        return Response(serializer.data)
    
    def post(self, request, format =  None):
        serializer = PollSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response({"msg":"Success"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"error":"Failed"}, status = status.HTTP_404_NOT_FOUND)
        

class PollDetails(APIView):
    def get(self, request, id = None):
        polls = get_object_or_404(Poll, id = id)
        serializer = PollSerializer(polls, many = False)
        return Response(serializer.data)
    

    def put(self, request, format = None):
        serializer = PollSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg":"Success"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"error":"Failed"}, status = status.HTTP_404_NOT_FOUND)
        

    def patch(self, request, format = None):
        polls = get_object_or_404(Poll, id = id)
        serializer = PollSerializer(polls,data = request.data, partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg":"Success"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"error":"Failed"}, status = status.HTTP_404_NOT_FOUND)
        

    def delete(self, request, id = None):
        polls = get_object_or_404(Poll, id = id)
        polls.delete()
        return Response({"msg":"deleted"}, status = status.HTTP_201_CREATED)
    

#with respect to the user
class PollSpecific(ListAPIView):
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]
    model = Poll
    
    def get_queryset(self):
        return self.model.objects.filter(created_by = self.request.user)