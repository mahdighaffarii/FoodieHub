from rest_framework import generics, permissions
from .models import Order, OrderItem
from .serializers import OrderCreateSerializer
from .serializers import OrderDisplaySerializer
from rest_framework import status as http_status
from rest_framework.views import APIView
from .serializers import OrderStatusUpdateSerializer
from rest_framework.generics import RetrieveAPIView
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from restaurants.models import Restaurant, FoodItem
from wallets.models import Wallet, Transaction # مدل Transaction را ایمپورت کنید
from .serializers import OrderCreateSerializer, OrderDisplaySerializer # سریالایزر جدید را ایمپورت کنید
from rest_framework import status # این خط را اضافه یا تکمیل کنید

class UpdateOrderStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        user = request.user
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=http_status.HTTP_404_NOT_FOUND)

        if user.role != 'RESTAURANT_MANAGER' or order.restaurant.manager != user:
            return Response({"error": "Unauthorized"}, status=http_status.HTTP_403_FORBIDDEN)

        serializer = OrderStatusUpdateSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=http_status.HTTP_200_OK)
        return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)

class ListUserOrdersView(generics.ListAPIView):
    serializer_class = OrderDisplaySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-created_at')


class CreateOrderView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        user = request.user
        
        # --- ۱. اعتبارسنجی‌های اولیه ---
        try:
            restaurant = Restaurant.objects.get(id=validated_data['restaurant_id'])
        except Restaurant.DoesNotExist:
            return Response({"error": "رستوران مورد نظر یافت نشد."}, status=status.HTTP_404_NOT_FOUND)

        # --- ۲. محاسبه قیمت کل و اعتبارسنجی آیتم‌ها ---
        total_price = 0
        order_items_data = []
        for item_data in validated_data['items']:
            try:
                food_item = FoodItem.objects.get(id=item_data['food_item_id'], restaurant=restaurant)
                if not food_item.is_available:
                     return Response({"error": f"غذای '{food_item.name}' در حال حاضر موجود نیست."}, status=status.HTTP_400_BAD_REQUEST)
            except FoodItem.DoesNotExist:
                return Response({"error": f"غذای با ID {item_data['food_item_id']} در این رستوران یافت نشد."}, status=status.HTTP_400_BAD_REQUEST)
            
            price = food_item.price * item_data['quantity']
            total_price += price
            order_items_data.append({'food_item': food_item, 'quantity': item_data['quantity'], 'price': food_item.price})

        # --- ۳. بررسی موجودی کیف پول ---
        user_wallet = user.wallet
        if user_wallet.balance < total_price:
            return Response({"error": "موجودی کیف پول برای این سفارش کافی نیست."}, status=status.HTTP_400_BAD_REQUEST)

        # --- ۴. اجرای عملیات دیتابیس (همه یا هیچ) ---
        # کسر از موجودی کیف پول
        user_wallet.balance -= total_price
        user_wallet.save()

        # ثبت تراکنش برداشت
        Transaction.objects.create(
            wallet=user_wallet,
            amount=total_price,
            transaction_type=Transaction.TransactionType.WITHDRAWAL,
            description=f"خرید از رستوران {restaurant.name}"
        )

        # ایجاد سفارش
        order = Order.objects.create(
            customer=user,  # در مدل شما customer نام دارد
            restaurant=restaurant,
            total_price=total_price,
            status='PENDING' # بر اساس مدل شما
        )

        # ایجاد آیتم‌های سفارش
        order_items_to_create = [
            OrderItem(
                order=order,
                food_item=item['food_item'],
                quantity=item['quantity'],
                price=item['price'] # قیمت در لحظه ثبت سفارش
            ) for item in order_items_data
        ]
        OrderItem.objects.bulk_create(order_items_to_create)

        # --- ۵. بازگرداندن نتیجه موفق ---
        # از سریالایزر نمایش برای بازگرداندن پاسخ استفاده می‌کنیم
        display_serializer = OrderDisplaySerializer(order)
        return Response(display_serializer.data, status=status.HTTP_201_CREATED)

class RestaurantOrdersView(generics.ListAPIView):
    serializer_class = OrderDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role != 'RESTAURANT_MANAGER':
            return Order.objects.none()
        return Order.objects.filter(restaurant__manager=user).order_by('-created_at')

class OrderDetailView(RetrieveAPIView):
    serializer_class = OrderDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

class CancelOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        user = request.user
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=http_status.HTTP_404_NOT_FOUND)

        if order.customer != user:
            return Response({"error": "Unauthorized"}, status=http_status.HTTP_403_FORBIDDEN)

        if order.status != Order.OrderStatus.PENDING:
            return Response({"error": "Only pending orders can be canceled"}, status=http_status.HTTP_400_BAD_REQUEST)

        order.status = Order.OrderStatus.CANCELED
        order.save()

        return Response({"message": "Order canceled successfully"}, status=http_status.HTTP_200_OK)