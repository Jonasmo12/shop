from django.test import TestCase, Client
from django.urls import reverse
from ...shop.models import Shop


class PaymentViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.shop = Shop.objects.create(
            name="discernd mega store",
            active=True
        )

    def test_template_used(self):
        response = self.client.get(
            reverse(
                'shop:payment:payment', kwargs={
                    'shop_slug': self.shop.slug
                }
            )
        )
        self.assertTemplateUsed(response, 'payment/payment.html')