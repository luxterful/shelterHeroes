from rest_framework import permissions, authentication, status
from rest_framework.response import Response
from rest_framework.views import APIView


from ShelterHeroesServer.core.models import Post

from ShelterHeroesServer.api.core.posts.serializers import PostSerializer


class FeedViewSet(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        obj = Post.objects.filter(posted_by__followed_by=request.user)
        serializer = PostSerializer(obj, many=True, context={"request": request})
        return Response(serializer.data)
