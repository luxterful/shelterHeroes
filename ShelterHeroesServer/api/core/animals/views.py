from django.http import Http404

from rest_framework import permissions, authentication, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from ShelterHeroesServer.core.models import Shelter, Animal, Post

from .serializers import AnimalSerializer


def get_object(pk):
    try:
        return Animal.objects.get(pk=pk)
    except Animal.DoesNotExist:
        raise Http404


class AnimalListViewSet(APIView):
    def get(self, request, format=None):
        paginator = PageNumberPagination()
        obj = Animal.objects.all()
        context = paginator.paginate_queryset(obj, request)
        serializer = AnimalSerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)


class AnimalViewSet(APIView):
    def get(self, request, pk, format=None):
        obj = get_object(pk=pk)
        serializer = AnimalSerializer(obj, context={"request": request})

        return Response(serializer.data)


class AnimalFollowViewSet(APIView):
    def post(self, request, pk, format=None):
        obj = get_object(pk=pk)
        obj.followed_by.add(request.user)

        return Response(status=status.HTTP_200_OK)


class AnimalUnfollowViewSet(APIView):
    def post(self, request, pk, format=None):
        obj = get_object(pk=pk)
        obj.followed_by.remove(request.user)

        return Response(status=status.HTTP_200_OK)
