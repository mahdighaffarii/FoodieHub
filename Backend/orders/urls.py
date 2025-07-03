from .views import CreateOrderView, ListUserOrdersView, RestaurantOrdersView, UpdateOrderStatusView

urlpatterns = [
    path('', CreateOrderView.as_view(), name='create_order'),
    path('my/', ListUserOrdersView.as_view(), name='my_orders'),  # /api/orders/my/
    path('restaurant/', RestaurantOrdersView.as_view(), name='restaurant_orders'),
    path('<int:pk>/update-status/', UpdateOrderStatusView.as_view(), name='update_order_status'),
]

