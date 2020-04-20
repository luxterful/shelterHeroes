from rest_framework import serializers
from django.core import exceptions
from django.conf import settings
from django.contrib.auth import authenticate

from ShelterHeroesServer.core.models import Shelter, Animal, Post, Comment
from ShelterHeroesServer.users.models import User
from ShelterHeroesServer.storage.models import PostImage


class PostShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ["pk", "name"]


class PostAnimalSerializer(serializers.ModelSerializer):
    shelter = PostShelterSerializer(read_only=True)

    class Meta:
        model = Animal
        fields = ["pk", "name", "shelter"]


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["text", "user"]


class PostImageSerializer(serializers.ModelSerializer):
    image_file = serializers.SerializerMethodField()

    class Meta:
        model = PostImage
        fields = ["image_file"]

    def get_image_file(self, obj):
        return obj.image_file.url


class PostSerializer(serializers.ModelSerializer):
    posted_by = PostAnimalSerializer(read_only=True)
    comments = PostCommentSerializer(read_only=True, many=True)
    image = PostImageSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    liked_by_viewer = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.liked_by.count()

    def get_liked_by_viewer(self, obj):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            return obj.liked_by.filter(pk=user.pk).first() != None
        return False

    class Meta:
        model = Post
        fields = [
            "pk",
            "likes_count",
            "liked_by_viewer",
            "text",
            "image",
            "posted_by",
            "comments",
        ]
