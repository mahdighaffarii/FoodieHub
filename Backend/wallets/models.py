# wallets/models.py
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Wallet(models.Model):
    # هر کاربر فقط یک کیف پول دارد
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.email}'s Wallet"

# این یک "سیگنال" است. به محض اینکه یک کاربر جدید در دیتابیس ذخیره می‌شود، این تابع فراخوانی می‌شود
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_wallet(sender, instance, created, **kwargs):
    # اگر کاربر جدیدی 'ایجاد' شده باشد
    if created:
        # فقط برای مشتریان کیف پول با موجودی اولیه ایجاد می‌کنیم
        if instance.role == 'CUSTOMER':
            Wallet.objects.create(user=instance, balance=1000000.00)
        else:
            Wallet.objects.create(user=instance) # برای مدیران کیف پول با موجودی صفر