from django.contrib import admin
from .models import Restaurant, Category, FoodItem

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(FoodItem)