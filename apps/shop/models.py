from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ..accounts.models import Account


class BankingInformation(models.Model):
    name = models.CharField(max_length=255)
    account_number = models.BigIntegerField()
    branch_code = models.BigIntegerField()
    account_type = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Address(models.Model):
    address1 = models.CharField('Address Line 1', max_length=255)
    address2 = models.CharField('Address Line 2', max_length=255, blank=True)
    suburb = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    post_code = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(
        max_length=10, help_text="Do not include country code, start with 0"
    )

    class Meta:
        abstract = True


class Shop(Address, Contact, BankingInformation):
    owner = models.OneToOneField(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    background_image = models.ImageField(
        upload_to="bg-images/", default="media/bg-images/default.jpg"
    )
    description = models.TextField()
    tag_line = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    shipping_fee = models.FloatField(null=True)

    class Meta:
        ordering = ['-created_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Shop, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'shop:shop', kwargs={'shop_slug': self.slug}
        )