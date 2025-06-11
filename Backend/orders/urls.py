from .views import CreateOrderView, ListUserOrdersView

urlpatterns = [
    path('', CreateOrderView.as_view(), name='create_order'),
    path('my/', ListUserOrdersView.as_view(), name='my_orders'),  # /api/orders/my/
]

