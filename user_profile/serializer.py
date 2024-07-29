from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User


# Registro de usuarios
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "phone",
            "is_admin",
        ]


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "user_profile"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user_profile_data = validated_data.pop("user_profile")
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, **user_profile_data)
        return user
