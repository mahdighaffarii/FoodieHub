# restaurants/models.py
from django.db import models
from django.conf import settings

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, unique=True)
    # هر رستوران یک مالک دارد که به مدل User ما (با نقش مدیر رستوران) متصل است
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='restaurant',
        limit_choices_to={'role': 'RESTAURANT_MANAGER'} # فقط کاربرانی با این نقش می‌توانند مالک باشند
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories" # برای نمایش صحیح در پنل ادمین

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) # برای قیمت از DecimalField استفاده کنید
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    # هر غذا به یک رستوران و یک دسته‌بندی تعلق دارد
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='food_items')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='food_items')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"