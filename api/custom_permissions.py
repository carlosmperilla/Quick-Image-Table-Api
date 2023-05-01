from django.core.exceptions import ValidationError

from rest_framework import permissions

from .models import Spacelimiter

class SpaceLimiterPermission(permissions.BasePermission):
    """
    Prevents data from being added or updated when 
    the allowed storage limit has been exceeded.
    """

    message = 'Cuota de almacenamiento excedida'

    def has_permission(self, request, view):

        SAFE_SPACE_METHODS = permissions.SAFE_METHODS + ('DELETE',)

        if not request.method in SAFE_SPACE_METHODS:
            if Spacelimiter.objects.exists():
                try:
                    Spacelimiter.objects.first().full_clean()
                except ValidationError:
                    return False
        
        return True