from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('isCart/', is_cart, name='is_cart_instance'),
    path('order/', CreateOrder.as_view(), name='order_received'),
    path('orders', OrdersList.as_view(), name='orders_list'),

]