from django.contrib import admin
from .models import Food

# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available', 'created_at')
    list_filter = ('is_available',)
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
