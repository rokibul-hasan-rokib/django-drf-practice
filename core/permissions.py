from rest_framework.permissions import BasePermission
from rolepermissions.checkers import has_permission

class HasCustomPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if hasattr(view, 'get_required_permission'):
            required_permission = view.get_required_permission()
        else:
            required_permission = getattr(view, 'required_permission', None)

        if required_permission:
            return has_permission(request.user, required_permission)
        return True  
