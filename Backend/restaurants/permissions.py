# restaurants/permissions.py
from rest_framework.permissions import BasePermission

class IsRestaurantManager(BasePermission):
    """
    Allows access only to authenticated users with the 'RESTAURANT_MANAGER' role.
    """
    def has_permission(self, request, view):
        # اول چک می‌کنیم که کاربر لاگین کرده باشد
        if not request.user or not request.user.is_authenticated:
            return False
        # سپس چک می‌کنیم که نقش او مدیر رستوران باشد
        return request.user.role == 'RESTAURANT_MANAGER'