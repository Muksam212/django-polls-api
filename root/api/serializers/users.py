from rest_framework import serializers
from users.models import User
from rest_framework.authtoken.models import Token

from ..serializers.polls import PollSerializer

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password":{"write_only":True}}


    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data["username"],
            email = validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        #Using token    
        Token.objects.create(user = user)
        return user


class UserListSerializer(serializers.ModelSerializer):
    #nested serializers
    user_created = PollSerializer(many = True)
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = User
        fields = ("id", "username", "email","user_created")



class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ("username", "password")


class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["old_password", "password", "confirm_password"]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"error": "The Password confirmation does not match"}
            )

        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError({"error": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
    

#UserProfile
class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = User
        fields = ("id", "username", "email")