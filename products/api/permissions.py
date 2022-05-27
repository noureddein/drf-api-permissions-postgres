from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Who can access the records in database
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
