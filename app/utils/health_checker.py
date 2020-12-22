from django.db import connections

# from django.db.utils import OperationalError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions


class HealthCheckerView(APIView):
    swagger_schema = None
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        print('Health Check...')
        db_conn = connections["default"]
        db_conn.cursor()
        return Response(request.jwt, status=status.HTTP_200_OK)
