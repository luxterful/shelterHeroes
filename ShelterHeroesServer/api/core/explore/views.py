from rest_framework import permissions, authentication, status
from rest_framework.response import Response
from rest_framework.views import APIView


from ShelterHeroesServer.core.models import Post, Animal

from ShelterHeroesServer.api.core.animals.serializers import AnimalSerializer


class ExploreViewSet(APIView):
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):

        query = request.GET.get("q")
        if query == None:
            query = ""

        obj = Animal.objects.filter(name__icontains=query)

        serializer = AnimalSerializer(obj, many=True)
        return Response(serializer.data)
