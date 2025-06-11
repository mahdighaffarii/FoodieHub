from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderCreateSerializer
from .serializers import OrderDisplaySerializer
from rest_framework.permissions import IsAuthenticated

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
