from django.db import connections
from django.db.utils import OperationalError
from django.core.management import call_command
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
import uuid


class LoadFixturesView(APIView):
    swagger_schema = None
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        db_conn = connections["default"]
        db_conn.cursor()
        call_command("loaddata", "fixtures/user.json", verbosity=0)
        return Response("OK", status=status.HTTP_200_OK)
