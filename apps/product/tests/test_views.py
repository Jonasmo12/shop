from django.test import TestCase, Client
from django.urls import reverse
from ..models import Product
from ...shop.models import Shop


class ProductTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.shop = Shop.objects.create(
			id=22,
			name="jumpman hyper",
			active=True,
		)
			
		self.product = Product.objects.create(
			id=12,
			title="Carpro Essence polish",
			shop=self.shop,
			price=899.99
		)

	def test_get(self):
		response = self.client.get(reverse('product:product', kwargs={'shop_slug': self.shop.slug, 'product_id': self.product.id}))
		self.assertEquals(response.status_code, 200)
