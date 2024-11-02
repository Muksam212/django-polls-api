from ..serializers.users import (
    UserRegisterSerializer,
    UserListSerializer, 
    UserPasswordResetSerializer,
    UserProfileSerializer
)
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .permission import IsOwner

from django.contrib.auth import authenticate
from users.models import User

from .filters import UserFilter
from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token

class UserRegisterAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    def post(self, request, format = None):
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response({"msg":"success"}, status = status.HTTP_200_OK)
        else:
            return Response({"error":"Failed"}, status = status.HTTP_404_NOT_FOUND)
        

class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
    
    def get_queryset(self):
        queryset = User.objects.all()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(Q(username__icontains = q) |
                                       Q(email__icontains = q))
        return queryset

class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username = username, password = password)
        
        if user:
            token, created = Token.objects.get_or_create(user = user)
            return Response({"token":token.key}, status = status.HTTP_200_OK)
        else:
            return Response({"error":"Wrong Credential"}, status = status.HTTP_404_NOT_FOUND)
        

class UserPasswordResetAPIView(UpdateAPIView):
    serializer_class = UserPasswordResetSerializer
    permission_classes = [IsAuthenticated]
    model = User
    lookup_field = "id"

    def get_queryset(self, queryset = None):
        return self.model.objects.filter(id = self.request.user.id)
    
    def update(self, request, *args, **kwargs):
        #calling the superclass update method to perform the update
        response = super().update(request, *args, **kwargs)

        #Customized the response to add a success message
        return Response({
            "message":"Password Reset Successful"
        }, status = status.HTTP_200_OK)
    

class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    

class EditProfileAPIView(UpdateAPIView):
    permission_classes = [IsOwner]
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data = request.data, partial = partial)

        serializer.is_valid(raise_exception = True)
        self.perform_update(serializer)

        return Response({
            "msg":"Profile Update Successful"
        }, status = status.HTTP_200_OK)
    

class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user = request.user)
            token.delete()
            return Response({"msg":"Successfully logout"}, status = status.HTTP_201_CREATED)
        except Token.DoesNotExist:
            return Response({"error":"Token not found"}, status = status.HTTP_404_NOT_FOUND)