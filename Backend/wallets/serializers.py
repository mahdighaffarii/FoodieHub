# wallets/serializers.py
from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    # با استفاده از source، مقدار خوانا (get_..._display) را برای transaction_type برمی‌گردانیم
    transaction_type_display = serializers.CharField(source='get_transaction_type_display', read_only=True)
    
    class Meta:
        model = Transaction
        # فیلدهایی که می‌خواهیم در پاسخ API نمایش داده شوند
        fields = [
            'id',
            'amount',
            'transaction_type',
            'transaction_type_display', # نام فارسی نوع تراکنش
            'description',
            'created_at'
        ]