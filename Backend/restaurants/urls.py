# restaurants/urls.py
from django.urls import path
from .views import RestaurantListView, RestaurantDetailView, CreateFoodItemView

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurant-list'),
    path('<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('foods/', CreateFoodItemView.as_view(), name='create_food'),
]