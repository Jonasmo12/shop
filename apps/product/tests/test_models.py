from django.test import TestCase
from ..models import Product, Tag
from ...shop.models import Shop

class ProductTest(TestCase):

    def setUp(self):
        self.shop = Shop.objects.create(
            name="skipper",
            owner="",
            active=True,
        )

        self.product = Product.objects.create(
            title="Jimmy Shoes",
            image="",
            price=1499.99,
            shop=self.shop,

        )