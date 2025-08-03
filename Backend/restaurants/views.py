# restaurants/views.py
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from .models import Restaurant, FoodItem
from .serializers import RestaurantListSerializer, RestaurantDetailSerializer, FoodItemCreateSerializer, FoodItemSerializer
from rest_framework.exceptions import PermissionDenied
from django.db.models import Q
from rest_framework import generics, permissions
from .serializers import RestaurantCreateSerializer # ایمپورت سریالایزر جدید
from .permissions import IsRestaurantManager

class RestaurantListView(generics.ListAPIView):
    """
    API view to list all active restaurants.
    """
    # فقط رستوران‌های فعال را نشان می‌دهیم
    queryset = Restaurant.objects.filter(is_active=True)
    serializer_class = RestaurantListSerializer
    permission_classes = [AllowAny] # به هر کسی اجازه دسترسی می‌دهیم

class RestaurantDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve details of a single restaurant, including its menu.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'



class CreateFoodItemView(generics.CreateAPIView):
    serializer_class = FoodItemCreateSerializer
    permission_classes = [permissions.IsAuthenticated, IsRestaurantManager] 

    def perform_create(self, serializer):
        user = self.request.user
        try:
            # اینجا باید از 'owner' استفاده شود، نه 'manager'
            restaurant = Restaurant.objects.get(owner=user)
        except Restaurant.DoesNotExist:
            raise PermissionDenied("شما رستورانی برای افزودن غذا ندارید. ابتدا رستوران خود را ثبت کنید.")
        
        serializer.save(restaurant=restaurant)

class UpdateDeleteFoodItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        food = self.get_object()
        user = self.request.user
        if food.restaurant.manager != user:
            raise PermissionDenied("You can only update your own food items.")
        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.restaurant.manager != user:
            raise PermissionDenied("You can only delete your own food items.")
        instance.delete()

class FoodSearchView(generics.ListAPIView):
    serializer_class = FoodItemSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return FoodItem.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query),
            is_available=True
        ).order_by('name')
        
class CreateRestaurantView(generics.CreateAPIView):
    """
    API view for restaurant managers to create their own restaurant.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateSerializer
    # اینجا از پرمیشن سفارشی خودمان استفاده می‌کنیم
    permission_classes = [permissions.IsAuthenticated, IsRestaurantManager]

    def perform_create(self, serializer):
        # این متد قبل از ذخیره کردن فراخوانی می‌شود
        # ما اینجا به صورت خودکار مالک رستوران را کاربر لاگین کرده قرار می‌دهیم
        serializer.save(owner=self.request.user)