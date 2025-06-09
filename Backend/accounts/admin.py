from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# ما از UserAdmin پیش‌فرض استفاده می‌کنیم اما می‌توانیم آن را سفارشی‌سازی کنیم
# برای مثال، فیلد 'role' را به لیست نمایش و فیلترها اضافه کنیم
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'username', 'name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser', 'groups')
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
    )

admin.site.register(User, CustomUserAdmin)