from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from products.models import Product


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_delivered = models.BooleanField(default=False)
    price_total = models.FloatField(default=0, null=True, blank=True)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name='order_product', on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, related_name='order_product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_subtotal = models.FloatField()







