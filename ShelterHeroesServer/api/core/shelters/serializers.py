from rest_framework import serializers
from django.core import exceptions
from django.conf import settings
from django.contrib.auth import authenticate

from ShelterHeroesServer.core.models import Shelter, Animal, Post, Comment
from ShelterHeroesServer.users.models import User

from ShelterHeroesServer.api.core.posts.serializers import PostImageSerializer


class AnimalPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["image", "text"]


class AnimalSerializer(serializers.ModelSerializer):
    recent_posts = serializers.SerializerMethodField(source="posts")
    image = PostImageSerializer(read_only=True)

    def get_recent_posts(self, obj):
        return AnimalPostSerializer(
            Post.objects.filter(posted_by=obj)[0:2], read_only=True, many=True
        ).data

    class Meta:
        model = Animal
        fields = ["pk", "name", "race", "recent_posts", "image"]


class ShelterSerializer(serializers.ModelSerializer):
    has_animals = AnimalSerializer(read_only=True, many=True)

    class Meta:
        model = Shelter
        fields = ["pk", "name", "address", "has_animals"]
