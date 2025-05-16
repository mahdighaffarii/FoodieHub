from django.urls import path
from . import views

app_name = 'foodapp'

urlpatterns = [
    path('foods/', views.food_list, name='food_list'),
    path('foods/<int:food_id>/', views.food_detail, name='food_detail'),
] 