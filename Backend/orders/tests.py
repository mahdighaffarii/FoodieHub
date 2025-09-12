# orders/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from restaurants.models import Restaurant, FoodItem, Category
from wallets.models import Wallet
from decimal import Decimal 

User = get_user_model()

class OrderCreationTests(APITestCase):
    
    def setUp(self):
        """
        این متد قبل از اجرای هر تست فراخوانی می‌شود و داده‌های اولیه را می‌سازد.
        """
        # ۱. ساخت کاربر مشتری
        self.customer = User.objects.create_user(
            email='customerfortest@example.com',
            username='customerfortest',
            password='testpassword',
            role='CUSTOMER'
        )
        # کیف پول به صورت خودکار با سیگنال ساخته می‌شود
        self.customer_wallet = Wallet.objects.get(user=self.customer)
        self.assertEqual(self.customer_wallet.balance, Decimal('1000000.00'))

        # ۲. ساخت کاربر مدیر رستوران
        self.manager = User.objects.create_user(
            email='managerfortest@example.com',
            username='managerfortest',
            password='testpassword',
            role='RESTAURANT_MANAGER'
        )

        # ۳. ساخت رستوران و غذا
        self.restaurant = Restaurant.objects.create(
            name='رستوران تستی',
            address='آدرس تستی',
            phone_number='0987654321',
            owner=self.manager
        )
        self.category = Category.objects.create(name='پیتزا تستی')
        self.food_item = FoodItem.objects.create(
            name='پیتزا تستی',
            price=Decimal('150000.00'), 
            restaurant=self.restaurant,
            category=self.category
        )

    def test_create_order_successfully(self):
        """
        Ensure a customer can create an order with sufficient funds.
        """
        # آدرس URL را پیدا می‌کنیم
        url = reverse('create-order')
        
        # با کاربر مشتری لاگین می‌کنیم
        self.client.force_authenticate(user=self.customer)
        
        # داده‌های سفارش را آماده می‌کنیم
        order_data = {
            "restaurant_id": self.restaurant.id,
            "items": [
                {
                    "food_item_id": self.food_item.id,
                    "quantity": 2
                }
            ]
        }

        # درخواست POST را ارسال می‌کنیم
        response = self.client.post(url, order_data, format='json')

        # بررسی نتایج
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # بررسی می‌کنیم که آیا قیمت کل درست محاسبه شده است (2 * 150,000 = 300,000)
        self.assertEqual(Decimal(response.data['total_price']), Decimal('300000.00'))
        
        # کیف پول را دوباره از دیتابیس می‌خوانیم تا مطمئن شویم موجودی کم شده است
        self.customer_wallet.refresh_from_db()
        self.assertEqual(self.customer_wallet.balance, Decimal('700000.00'))



