# wallets/views.py
from rest_framework import generics, permissions
from .models import Transaction
from .serializers import TransactionSerializer

class WalletTransactionHistoryView(generics.ListAPIView):
    """
    API view to list all transactions for the currently authenticated user's wallet.
    """
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # کوئری را طوری فیلتر می‌کنیم که فقط تراکنش‌های مربوط به
        # کیف پول کاربر لاگین کرده را برگرداند.
        # ordering هم تضمین می‌کند که جدیدترین‌ها اول نمایش داده شوند.
        return Transaction.objects.filter(wallet__user=self.request.user).order_by('-created_at')