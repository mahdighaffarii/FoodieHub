from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView, # این ویو برای لاگین و گرفتن توکن است
    TokenRefreshView,    # این ویو برای تمدید توکن است
)
from django.conf.urls.static import static


urlpatterns = [
    path('register/', RegisterView.as_view(), name='user_register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

