from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view, *args, **kwargs):
        return request.jwt and request.jwt.get("is_superuser") is True


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view, *args, **kwargs):
        return request.jwt is not None


class AllowAny(permissions.BasePermission):
    def has_permission(self, request, view, *args, **kwargs):
        return True
