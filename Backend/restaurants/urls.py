# restaurants/urls.py
from django.urls import path
# ایمپورت کردن تمام ویوها
from .views import (
    RestaurantListView, 
    RestaurantDetailView, 
    CreateRestaurantView,
    CreateFoodItemView,
    UpdateDeleteFoodItemView,
    FoodSearchView
)

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurant-list'),
    path('create/', CreateRestaurantView.as_view(), name='restaurant-create'),
    path('<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('foods/create/', CreateFoodItemView.as_view(), name='food-create'),
    path('foods/<int:pk>/', UpdateDeleteFoodItemView.as_view(), name='food-detail-update-delete'),
    path('foods/search/', FoodSearchView.as_view(), name='food_search'),
    ]