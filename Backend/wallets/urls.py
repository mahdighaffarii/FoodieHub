from django.urls import path
from .views import WalletTransactionHistoryView

urlpatterns = [
    path('history/', WalletTransactionHistoryView.as_view(), name='wallet-history'),
]