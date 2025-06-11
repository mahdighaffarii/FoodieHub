from rest_framework import serializers
from .models import Order, OrderItem
from wallets.models import Wallet 
from restaurants.models import FoodItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['food_item', 'quantity']


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)  # دریافت آیتم‌ها از فرانت

    class Meta:
        model = Order
        fields = ['restaurant', 'items']  # کاربر خودش از request میاد، total_price محاسبه میشه

    def validate(self, data):
        # محاسبه قیمت کل
        total_price = 0
        for item in data['items']:
            food = item['food_item']
            total_price += food.price * item['quantity']

        # بررسی موجودی کیف پول
        user = self.context['request'].user
        if not hasattr(user, 'wallet'):
            raise serializers.ValidationError("کاربر کیف پول ندارد.")
        if user.wallet.balance < total_price:
            raise serializers.ValidationError("موجودی کیف پول کافی نیست.")

        data['total_price'] = total_price  # اضافه کنیم که تو create استفاده شه
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        restaurant = validated_data['restaurant']
        items_data = validated_data.pop('items')
        total_price = validated_data.pop('total_price')

        # ایجاد سفارش
        order = Order.objects.create(
            customer=user,
            restaurant=restaurant,
            total_price=total_price
        )

        # ایجاد آیتم‌ها
        for item in items_data:
            OrderItem.objects.create(
                order=order,
                food_item=item['food_item'],
                quantity=item['quantity']
            )

        # کم کردن از کیف پول
        user.wallet.withdraw(total_price)

        return order
