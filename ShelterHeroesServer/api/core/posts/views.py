from django.http import Http404

from rest_framework import permissions, authentication, status
from rest_framework.response import Response
from rest_framework.views import APIView


from ShelterHeroesServer.core.models import Shelter, Animal, Post

from .serializers import PostSerializer, CreatePostCommentSerializer


def get_object(pk):
    try:
        return Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404


class PostViewSet(APIView):
    def get(self, request, pk, format=None):
        obj = get_object(pk=pk)
        serializer = PostSerializer(obj, context={"request": request})

        return Response(serializer.data)


class PostLikeViewSet(APIView):
    def post(self, request, pk, format=None):
        obj = get_object(pk=pk)
        obj.liked_by.add(request.user)

        return Response(status=status.HTTP_200_OK)


class PostUnlikeViewSet(APIView):
    def post(self, request, pk, format=None):
        obj = get_object(pk=pk)
        obj.liked_by.remove(request.user)

        return Response(status=status.HTTP_200_OK)


class PostCommentViewSet(APIView):
    def post(self, request, pk, format=None):
        serializer = CreatePostCommentSerializer(
            data={
                "user": request.user.pk,
                "post": get_object(pk=pk).pk,
                "text": request.data.get("text"),
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
