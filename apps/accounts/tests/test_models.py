from django.test import TestCase
from ..models import Account


class TestAccount(TestCase):

    def test_account_fields(self):
        field_names = [
            field.name for field in Account._meta.get_fields()
        ]
        self.assertIn('email', field_names), 'returns true, if fields are present'
        self.assertIn('first_name', field_names)
        self.assertIn('last_name', field_names)

    def setUp(self):
        self.account = Account.objects.create(
            id=11,
            first_name="James",
            last_name="Mo",
            email="James@email.com",
            is_staff=True,
        )

    def test_model_instance(self):
        self.assertIsInstance(self.account, Account), "should return true, user created"

    def test_created_user(self):
        self.assertEquals(self.account.id, 11)

    def test_superuser_status(self):
        self.assertEquals(self.account.is_staff, True)

    def test_verbose_name_plural(self):
        self.assertEquals("accounts", str(self.account._meta.verbose_name_plural))

    def test_str_method(self):
        self.assertEquals(self.account.__str__(), "James Mo, James@email.com")