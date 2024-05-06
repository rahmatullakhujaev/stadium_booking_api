from rest_framework.permissions import BasePermission



class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role.code_name == 'admin'


class IsStadiumOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role.code_name == 'stadium owner'


class IsAdminOrStadiumOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role.code_name in ('stadium owner', 'admin')

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role.code_name == 'user'

