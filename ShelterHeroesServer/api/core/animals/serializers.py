from rest_framework import serializers

from ShelterHeroesServer.core.models import Shelter, Animal, Post
from ShelterHeroesServer.users.models import User

from ShelterHeroesServer.api.core.shelters.serializers import ShelterSerializer
from ShelterHeroesServer.api.core.posts.serializers import PostImageSerializer


class RecentPostSerializer(serializers.ModelSerializer):
    image = PostImageSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ["pk", "image"]


class AnimalSerializer(serializers.ModelSerializer):
    recent_posts = serializers.SerializerMethodField(source="posts")
    shelter = ShelterSerializer(read_only=True)
    followed_by_viewer = serializers.SerializerMethodField()
    image = PostImageSerializer(read_only=True)

    def get_recent_posts(self, obj):
        return RecentPostSerializer(
            Post.objects.filter(posted_by=obj), read_only=True, many=True
        ).data

    def get_followed_by_viewer(self, obj):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            return obj.followed_by.filter(pk=user.pk).first() != None
        return False

    class Meta:
        model = Animal
        fields = [
            "pk",
            "name",
            "shelter",
            "recent_posts",
            "followed_by_viewer",
            "image",
        ]
