from decimal import Decimal

from django.conf import settings
from django.db import models
from ..product.models import Product


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    price = models.FloatField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)