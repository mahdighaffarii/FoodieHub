from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderCreateSerializer
from .serializers import OrderDisplaySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status as http_status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import OrderStatusUpdateSerializer

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


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # ارسال کاربر فعلی برای استفاده در serializer
        serializer.save()

class RestaurantOrdersView(generics.ListAPIView):
    serializer_class = OrderDisplaySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role != 'RESTAURANT_MANAGER':
            return Order.objects.none()
        return Order.objects.filter(restaurant__manager=user).order_by('-created_at')
