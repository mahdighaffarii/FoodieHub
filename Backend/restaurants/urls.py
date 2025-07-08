# restaurants/urls.py
from django.urls import path
from .views import RestaurantListView, RestaurantDetailView, CreateFoodItemView, UpdateDeleteFoodItemView, FoodSearchView

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurant-list'),
    path('<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('foods/', CreateFoodItemView.as_view(), name='create_food'),
    path('foods/<int:pk>/', UpdateDeleteFoodItemView.as_view(), name='update_delete_food'),
    path('foods/search/', FoodSearchView.as_view(), name='food_search'),
    ]