from django.test import TestCase
from ..models import Shop


class ShopTest(TestCase):

    def setUp(self):
        self.shop = Shop.objects.create(
            id=12,
            name="shop 1",
            active=True,
        )
    
    def test_instance(self):
        self.assertIsInstance(self.shop, Shop)

    def test_obj_created(self):
        self.assertEquals(self.shop.id, 12)
        self.assertEquals(self.shop.active, True)

    def test_slug(self):
        self.assertEquals(self.shop.slug, "shop-1")

    def test__string_represention(self):
        self.assertEquals(self.shop.__str__(), 'shop 1')



    