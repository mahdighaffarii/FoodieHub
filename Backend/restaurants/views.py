# restaurants/views.py
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from .models import Restaurant, FoodItem
from .serializers import RestaurantListSerializer, RestaurantDetailSerializer, FoodItemCreateSerializer, FoodItemSerializer
from rest_framework.exceptions import PermissionDenied
from django.db.models import Q
from rest_framework import generics, permissions
from .serializers import RestaurantCreateSerializer # ایمپورت سریالایزر جدید
from .permissions import IsRestaurantManager
from .models import Category
from .serializers import CategorySerializer
from rest_framework.exceptions import PermissionDenied


class RestaurantListView(generics.ListAPIView):
    """
    API view to list all active restaurants.
    """
    # فقط رستوران‌های فعال را نشان می‌دهیم
    queryset = Restaurant.objects.filter(is_active=True)
    serializer_class = RestaurantListSerializer
    permission_classes = [AllowAny] # به هر کسی اجازه دسترسی می‌دهیم

class RestaurantDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve details of a single restaurant, including its menu.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'



class CreateFoodItemView(generics.CreateAPIView):
    serializer_class = FoodItemCreateSerializer
    permission_classes = [permissions.IsAuthenticated, IsRestaurantManager] 

    def perform_create(self, serializer):
        user = self.request.user
        try:
            # اینجا باید از 'owner' استفاده شود، نه 'manager'
            restaurant = Restaurant.objects.get(owner=user)
        except Restaurant.DoesNotExist:
            raise PermissionDenied("شما رستورانی برای افزودن غذا ندارید. ابتدا رستوران خود را ثبت کنید.")
        
        serializer.save(restaurant=restaurant)

class UpdateDeleteFoodItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemCreateSerializer # یا FoodItemSerializer
    # ما از پرمیشن IsRestaurantManager استفاده می‌کنیم تا مطمئن شویم فقط مدیران به این API دسترسی دارند
    permission_classes = [permissions.IsAuthenticated, IsRestaurantManager]

    def get_queryset(self):
        """
        این متد queryset را محدود می‌کند تا یک مدیر فقط بتواند
        آیتم‌های منوی رستوران خودش را ببیند/ویرایش/حذف کند.
        """
        user = self.request.user
        if user.role == 'RESTAURANT_MANAGER':
            return FoodItem.objects.filter(restaurant__owner=user)
        return FoodItem.objects.none() # برای دیگران، هیچ چیزی برنگردان

    # با وجود get_queryset، دیگر نیازی به بازنویسی perform_update و perform_destroy نیست!
    # DRF به صورت خودکار چک می‌کند که آیا آبجکت در queryset موجود است یا نه.
    # اما برای اطمینان بیشتر، می‌توانیم آنها را نگه داریم و اصلاح کنیم.

    def perform_update(self, serializer):
        food = self.get_object()
        user = self.request.user
        # کد اصلاح شده:
        if food.restaurant.owner != user:
            raise PermissionDenied("شما فقط می‌توانید آیتم‌های منوی خودتان را ویرایش کنید.")
        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user
        # کد اصلاح شده:
        if instance.restaurant.owner != user:
            raise PermissionDenied("شما فقط می‌توانید آیتم‌های منوی خودتان را حذف کنید.")
        instance.delete()

class FoodSearchView(generics.ListAPIView):
    serializer_class = FoodItemSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return FoodItem.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query),
            is_available=True
        ).order_by('name')
        
class CreateRestaurantView(generics.CreateAPIView):
    """
    API view for restaurant managers to create their own restaurant.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateSerializer
    # اینجا از پرمیشن سفارشی خودمان استفاده می‌کنیم
    permission_classes = [permissions.IsAuthenticated, IsRestaurantManager]

    def perform_create(self, serializer):
        # این متد قبل از ذخیره کردن فراخوانی می‌شود
        # ما اینجا به صورت خودکار مالک رستوران را کاربر لاگین کرده قرار می‌دهیم
        serializer.save(owner=self.request.user)
        

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated] # فقط کاربران لاگین 
    
    
class ManagerMenuView(generics.ListAPIView):
    serializer_class = FoodItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsRestaurantManager]

    def get_queryset(self):
        # فقط غذاهای مربوط به رستورانِ مدیر فعلی را برمی‌گرداند
        return FoodItem.objects.filter(restaurant__owner=self.request.user)