from django.http import Http404

from rest_framework import permissions, authentication, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from ShelterHeroesServer.core.models import Shelter, Animal

from .serializers import ShelterSerializer, AnimalSerializer


class ShelterViewSet(APIView):
    def get_object(self, pk):
        try:
            return Shelter.objects.get(pk=pk)
        except Shelter.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk=pk)
        serializer = ShelterSerializer(obj)

        return Response(serializer.data)


class ShelterListViewSet(APIView):
    def get(self, request, format=None):
        paginator = PageNumberPagination()
        obj = Shelter.objects.all()
        context = paginator.paginate_queryset(obj, request)
        serializer = ShelterSerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)


class AnimalListViewSet(APIView):
    def get(self, request, pk, format=None):
        paginator = PageNumberPagination()
        obj = Animal.objects.filter(shelter=pk)
        context = paginator.paginate_queryset(obj, request)
        serializer = AnimalSerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)
