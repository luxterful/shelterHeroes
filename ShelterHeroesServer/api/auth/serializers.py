from django.contrib.auth.models import Group
from rest_framework import serializers
from django.core import exceptions
from django.conf import settings
from django.contrib.auth import authenticate

from ShelterHeroesServer.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "username", "full_name"]


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "full_name", "password")
        write_only_fields = ("password",)

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data["email"],
            full_name=validated_data["full_name"],
            password=validated_data["password"],
        )


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate(self, attrs):
        user = authenticate(username=attrs["email"], password=attrs["password"])

        if not user:
            raise serializers.ValidationError("Incorrect email or password.")

        if not user.is_active:
            raise serializers.ValidationError("User is disabled.")

        user.backend = settings.AUTHENTICATION_BACKENDS[0]

        return {"user": user}
