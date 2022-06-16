from django.test import TestCase
from mixer.backend.django import mixer
from ..models import Account




class TestAccount(TestCase):
    #def test_account_fields(self):
        # field_names = [
        #     field.name for field in Account._meta.get_fields()
        # ]
        # expected_field_names = [
        #     "id",
        #     "email",
        #     "is_staff"
        # ]
        # assert field_names == expected_field_names, 'returns true, if fields are present'

    # def test_fields(self):
    #     obj = mixer.blend(Account)
    #     assert isinstance(obj.first_name, str)
    #     assert isinstance(obj.last_name, str)
    #     assert isinstance(obj.is_student, boolean)
    #     assert isinstance(obj.date_joined, datetime)

    def test_model_instance(self):
        account = mixer.blend(Account)
        self.assertIsInstance(account, Account), "should return true, user created"

    def test_created_user(self):
        account = mixer.blend(Account, id=1)
        self.assertEquals(account.id, 1)

    def test_superuser_status(self):
        account = mixer.blend(Account)
        assert account.is_superuser == False

    def test_verbose_name_plural(self):
        assert "accounts" == str(Account._meta.verbose_name_plural)

    def test_verbose_name(self):
        assert "account" == str(Account._meta.verbose_name)

    def test_str_method(self):
        obj = mixer.blend(Account)
        account = f"{obj.first_name} {obj.last_name}, {obj.email}"
        assert str(obj) == account