"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from utils.health_checker import HealthCheckerView
from utils.load_fixtures import LoadFixturesView
from utils.migration import MigrationView
import os

urlpatterns = [
    re_path(r"^api/migrate/?$", MigrationView.as_view()),
    re_path(r"^api/health/?$", HealthCheckerView.as_view()),
]

# DOC SWAGGER SETTINGS
if os.getenv("ENVIRONMENT") != "prod":

    # DJANGO STATIC URLS
    urlpatterns += staticfiles_urlpatterns()

    schema_view = get_schema_view(
        openapi.Info(
            title="PHP API",
            default_version="v1",
            description="PHP API",
            terms_of_service="",
            contact=openapi.Contact(email="aimonbio@gmail.com"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )
    urlpatterns += [
        path(
            "swagger",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
        path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    ]

    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

urlpatterns = format_suffix_patterns(urlpatterns)

