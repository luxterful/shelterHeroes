from rest_framework import permissions, authentication, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.management import call_command


class InitViewset(APIView):
    def get(self, request, format=None):
        call_command("init_demo_db")
        return Response("done", status=200)
