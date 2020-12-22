from django.http import JsonResponse
import os
import jwt


class OAuth2Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        parts = str(request.headers.get("authorization", "")).split(" ")

        request.jwt = None
        if len(parts) == 2:
            try:
                request.jwt = jwt.decode(
                    parts[1], os.getenv("JWT_SECRET_KEY", ""), algorithms="HS256"
                )
            except:
                request.jwt = None

        response = self.get_response(request)

        return response
