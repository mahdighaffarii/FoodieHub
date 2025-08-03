from rest_framework import serializers
from .models import Order, OrderItem
from wallets.models import Wallet 
from restaurants.models import FoodItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['food_item', 'quantity']

class OrderItemCreateSerializer(serializers.Serializer):
    food_item_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)
    
class OrderCreateSerializer(serializers.Serializer):
    restaurant_id = serializers.IntegerField()
    items = OrderItemCreateSerializer(many=True)

    def validate_items(self, items):
        if not items:
            raise serializers.ValidationError("سبد خرید نمی‌تواند خالی باشد.")
        return items
    
    
class OrderItemDisplaySerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(source='food_item.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['food_name', 'quantity']

class OrderDisplaySerializer(serializers.ModelSerializer):
    items = OrderItemDisplaySerializer(many=True, read_only=True)
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'restaurant_name', 'total_price', 'status', 'created_at', 'items']

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

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']

    def validate_status(self, value):
        if value not in Order.OrderStatus.values:
            raise serializers.ValidationError("Invalid status value")
        return value

