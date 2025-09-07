# wallets/views.py
from rest_framework import generics, permissions
from .models import Transaction
from .serializers import TransactionSerializer

class WalletTransactionHistoryView(generics.ListAPIView):

    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(wallet__user=self.request.user).order_by('-created_at')