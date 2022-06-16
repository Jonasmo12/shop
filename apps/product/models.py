from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ..shop.models import Shop


class Product(models.Model):
    title = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/')
    in_stock = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, default="")
    slug = models.SlugField(null=True, unique=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self):
        return f"{self.title} <-> {self.shop}"

    def get_absolute_url(self):
        return reverse("product:product", kwargs={"product_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
