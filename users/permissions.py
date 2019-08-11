from rest_framework import permissions


class IsGlobalAdminStaff(permissions.BasePermission):
    message = "You do not have Admin Staff permissions"

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff
