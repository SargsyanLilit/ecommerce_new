from django.urls import path, include
from orders import views


urlpatterns = [
    path('', views.orders_list, name='orders'),
    # path('order-item/<int:product_id>/<int:quantity>', views.create_order_item, name='order-item'),
    path('order-item/<int:product_id>/', views.create_order_item, name='order-item'),
    path('delete-item/<int:order_id>/', views.order_item_delete, name='order-item-delete'),
]
