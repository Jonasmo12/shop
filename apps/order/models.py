from django.conf import settings
from django.db import models
from ..product.models import Product
from ..shop.models import Shop


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(null=True)
    post_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.FloatField(null=True)
    order_id = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    shop = models.ForeignKey(
        Shop, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.FloatField(null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)