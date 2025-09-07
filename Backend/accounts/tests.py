# accounts/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class AccountTests(APITestCase):
    
    def test_create_customer_account(self):
        """
        Ensure we can create a new customer account.
        """
        # آدرس URL را با استفاده از نام آن پیدا می‌کنیم تا اگر در آینده تغییر کرد، تست ما خراب نشود
        url = reverse('user_register') 
        
        # داده‌هایی که می‌خواهیم برای ثبت‌نام ارسال کنیم
        data = {
            'email': 'testcustomer@example.com',
            'username': 'testcustomer',
            'password': 'somepassword123',
            'name': 'تست مشتری',
            'role': 'CUSTOMER'
        }
        
        # ارسال درخواست POST به API
        response = self.client.post(url, data, format='json')
        
        # بررسی نتایج
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], 'testcustomer@example.com')
        self.assertNotIn('password', response.data) # مطمئن می‌شویم پسورد در پاسخ برگردانده نمی‌شود

    def test_login_user_and_get_token(self):
        """
        Ensure a registered user can log in and receive JWT tokens.
        """
        # ۱. ابتدا یک کاربر برای تست ایجاد می‌کنیم
        self.test_create_customer_account() # از تست قبلی برای ساخت کاربر استفاده می‌کنیم

        # ۲. آدرس URL لاگین را پیدا می‌کنیم
        url = reverse('token_obtain_pair')

        # ۳. داده‌های لاگین را آماده می‌کنیم
        data = {
            'email': 'testcustomer@example.com',
            'password': 'somepassword123'
        }

        # ۴. درخواست POST را ارسال می‌کنیم
        response = self.client.post(url, data, format='json')

        # ۵. نتایج را بررسی می‌کنیم
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data) # چک می‌کنیم که توکن access وجود دارد
        self.assertTrue('refresh' in response.data) # چک می‌کنیم که توکن refresh وجود دارد