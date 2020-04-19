from django.contrib.auth import login, logout

from rest_framework import permissions, authentication, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from ShelterHeroesServer.users.models import User

from .serializers import (
    UserSerializer,
    RegistrationSerializer,
    LoginSerializer,
)


class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            response_serializer = UserSerializer(
                instance=user, context={"request": request}
            )
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SigninView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        response_serializer = UserSerializer(
            instance=user, context={"request": request}
        )

        return Response(response_serializer.data, status=status.HTTP_200_OK)


class SignoutView(generics.CreateAPIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class AuthInfoView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response("{pk:null}")
        serializer = self.get_serializer(user)
        return Response(serializer.data)
