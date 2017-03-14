from rest_framework import permissions

class RequestPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):        
        return obj.first == request.user or obj.second == request.user or request.user.is_staff