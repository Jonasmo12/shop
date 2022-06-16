from django.test import TestCase, Client
from django.urls import reverse
from ..models import Account


class TestLoginView(TestCase):

	def setUp(self):
		self.client = Client()
		self.user = Account.objects.create(
			first_name="Jonny",
			last_name="Bango",
			email="Jonny@email.com",
			is_superuser=True,
			is_staff=True
		)
		self.user.set_password("Thaketse93")
		self.user.save()

	def test_response(self):
		response = self.client.get(reverse('accounts:login'))
		self.assertEquals(response.status_code, 200)

	def test_template_used(self):
		response = self.client.get(reverse('accounts:login'))
		self.assertTemplateUsed(response, 'accounts/login.html')

	def test_login(self):
		login = self.client.login(email="Jonny@email.com", password="Thaketse93")
		response = self.client.post(reverse("accounts:login"))
		self.assertEquals(response.status_code, 302)

	def test_redirect(self):
		login = self.client.login(email="Jonny@email.com", password="Thaketse93")
		response = self.client.post(reverse("accounts:login"), follow=True)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'home.html')
	

class TestLogout(TestCase):

	def setUp(self):
		self.client = Client()
		self.user = Account.objects.create(
			first_name="Jonny",
			last_name="Bango",
			email="Jonny@email.com",
			is_superuser=True,
			is_staff=True
		)
		self.user.set_password("Thaketse93")
		self.user.save()

	def test_logout(self):
		login = self.client.login(email="Jonny@email.com", password="Thaketse93")
		response = self.client.post(reverse("accounts:logout"))
		self.assertEquals(response.status_code, 302)

	def test_redirect(self):
		login = self.client.login(email="Jonny@email.com", password="Thaketse93")
		response = self.client.post(reverse("accounts:logout"), follow=True)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'home.html')