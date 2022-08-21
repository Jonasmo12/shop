from django.test import TestCase, Client
from ..models import Order, OrderItem
from ...shop.models import Shop
from ...product.models import Product


class OrderTest(TestCase):

    def setUp(self):
        self.shop = Shop.objects.create(name='studio 100')
        self.product1 = Product.objects.create(title='Jean', price=1299.99)
        self.product2 = Product.objects.create(title='Shirt', price=299.99)

        self.order = Order.objects.create(
            first_name="Jonny",
            last_name="Bango",
            shop=self.shop,
            order_id="11",
            complete=True,
        )

    def test_order_instance(self):
        self.assertIsInstance(self.order, Order)