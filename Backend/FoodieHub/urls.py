# FoodieHub/urls.py
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/restaurants/', include('restaurants.urls')), # این خط را اضافه کنید
]