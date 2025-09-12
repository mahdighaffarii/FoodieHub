# accounts/serializers.py
from rest_framework import serializers
from .models import User
from restaurants.serializers import SimpleRestaurantSerializer # ایمپورت


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'name', 'role')
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data.get('name', ''),
            role=validated_data.get('role', User.Role.CUSTOMER)
        )
        return user
    
# accounts/serializers.py
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'name', 'role')
        

class UserDetailSerializer(serializers.ModelSerializer):
    restaurant = SimpleRestaurantSerializer(read_only=True) # اضافه کردن فیلد رستوران
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'name', 'role', 'restaurant')