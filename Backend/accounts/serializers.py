# accounts/serializers.py
from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    # فیلد پسورد را فقط برای نوشتن (ایجاد کاربر) در نظر می‌گیریم
    # و در پاسخ API آن را بر نمی‌گردانیم.
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        # فیلدهایی که برای ثبت‌نام نیاز داریم
        fields = ('email', 'username', 'password', 'name', 'role')

    def create(self, validated_data):
        # متد create را بازنویسی می‌کنیم تا پسورد به درستی هش شود
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data.get('name', ''),
            role=validated_data.get('role', User.Role.CUSTOMER)
        )
        return user