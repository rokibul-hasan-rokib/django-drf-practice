from .permissions import HasCustomPermission
class PermissionRequiredMixin:
    permission_classes = [HasCustomPermission]
    required_permission = None

    def get_required_permission(self):
        """
        If not explicitly set, use dynamic permission based on model + action
        Example: 'add_product', 'view_product', etc.
        """
        if self.required_permission:
            return self.required_permission
        action_map = {
            'create': f"add_{self.queryset.model._meta.model_name}",
            'list': f"view_{self.queryset.model._meta.model_name}",
            'retrieve': f"view_{self.queryset.model._meta.model_name}",
            'update': f"change_{self.queryset.model._meta.model_name}",
            'partial_update': f"change_{self.queryset.model._meta.model_name}",
            'destroy': f"delete_{self.queryset.model._meta.model_name}",
        }
        return action_map.get(self.action)
