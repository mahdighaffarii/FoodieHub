# restaurants/serializers.py
from rest_framework import serializers
from .models import Restaurant, FoodItem, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class FoodItemSerializer(serializers.ModelSerializer):
    # برای نمایش نام دسته به جای آیدی آن
    category = CategorySerializer(read_only=True)

    class Meta:
        model = FoodItem
        fields = ['id', 'name', 'description', 'price', 'image', 'category', 'is_available']


# این سریالایزر برای نمایش لیست کلی رستوران‌ها استفاده می‌شود (اطلاعات خلاصه)
class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone_number', 'is_active']


# این سریالایزر برای نمایش جزئیات کامل یک رستوران به همراه منوی آن است
class RestaurantDetailSerializer(serializers.ModelSerializer):
    # از سریالایزر FoodItem برای نمایش لیست غذاها به صورت تو در تو (nested) استفاده می‌کنیم
    # many=True چون یک رستوران چندین غذا دارد
    # read_only=True چون این فیلد فقط برای نمایش است و از طریق این API ایجاد یا ویرایش نمی‌شود
    food_items = FoodItemSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone_number', 'owner', 'food_items']