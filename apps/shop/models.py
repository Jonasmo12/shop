from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ..accounts.models import Account


class Address(models.Model):
    address1 = models.CharField('Address Line 1', max_length=255, null=True)
    address2 = models.CharField('Address Line 2', max_length=255, null=True, blank=True)
    suburb = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    province = models.CharField(max_length=255, null=True)
    post_code = models.CharField(max_length=255, null=True)

    class Meta:
        abstract = True


class Contact(models.Model):
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=10, null=True)

    class Meta:
        abstract = True


class Shop(Address, Contact):
    owner = models.ForeignKey(
        Account, null=True, default="", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    background_image = models.ImageField(
        upload_to="bg-images/", default="media/bg-images/default.jpg"
    )
    description = models.TextField(default="")
    tag_line = models.CharField(max_length=255, default="")
    active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

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