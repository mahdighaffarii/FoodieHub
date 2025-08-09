from rest_framework import permissions

class IsOrderOwnerForManager(permissions.BasePermission):
    """
    Object-level permission to only allow managers of a restaurant
    to edit orders associated with it.
    """
    def has_object_permission(self, request, view, obj):
        # obj در اینجا همان شیء Order است
        if request.user.is_authenticated and request.user.role == 'RESTAURANT_MANAGER':
            return obj.restaurant.owner == request.user
        return False