from rest_framework.permissions import BasePermission
from .models import User

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class IsManager(BasePermission):
    def has_permission(self, request, view):
        # Implement logic to check if user has "Manager" role within their organization
        pass
class IsMember(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Organization):
            return request.user.is_superuser or obj.pk == request.user.organization.pk
        elif isinstance(obj, Role):
            return request.user.is_superuser or obj.organization.pk == request
