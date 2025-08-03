from django.db import models
from django.conf import settings
from restaurants.models import Restaurant, FoodItem

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'در انتظار پرداخت'),
        ('CONFIRMED', 'تأیید شده'),
        ('CANCELED', 'لغو شده'),
        ('SENT', 'ارسال شده'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.pk} - {self.customer.email} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت واحد (در زمان ثبت)")

    def __str__(self):
        # می‌توانید __str__ را هم به‌روز کنید
        return f"{self.quantity} x {self.food_item.name} @ {self.price}"