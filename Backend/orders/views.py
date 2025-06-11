from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderCreateSerializer

class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # ارسال کاربر فعلی برای استفاده در serializer
        serializer.save()
