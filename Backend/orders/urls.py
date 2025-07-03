from django.urls import path
from .views import CreateOrderView, ListUserOrdersView, RestaurantOrdersView, UpdateOrderStatusView, OrderDetailView, CancelOrderView

urlpatterns = [
    path('', CreateOrderView.as_view(), name='create_order'),
    path('my/', ListUserOrdersView.as_view(), name='my_orders'),  # /api/orders/my/
    path('restaurant/', RestaurantOrdersView.as_view(), name='restaurant_orders'),
    path('<int:pk>/update-status/', UpdateOrderStatusView.as_view(), name='update_order_status'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('<int:pk>/cancel/', CancelOrderView.as_view(), name='cancel_order'),
]

