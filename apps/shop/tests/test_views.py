from django.test import TestCase, Client
from django.urls import reverse
from ..models import Shop


class HomeViewTest(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse('shop:home'))
        self.assertTemplateUsed(response, 'home.html')


class ShopTest(TestCase):

    def setUp(self):
        self.shop = Shop.objects.create(
            id=123,
            name="jupman hyper",
            active=True,
        )

    def test_get_shop(self):
        response = self.client.get(reverse('shop:shop', kwargs={
                "shop_slug": self.shop.slug
        }))
        self.assertEquals(response.status_code, 200)