# restaurants/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Restaurant
from .serializers import RestaurantListSerializer, RestaurantDetailSerializer

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