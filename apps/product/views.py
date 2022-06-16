from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Product
from ..shop.models import Shop


class ProductDetailView(View):
    model = Product
    template_name = "product/product.html"
    
    def get(self, request, shop_slug, product_slug):
        shop = Shop.objects.get(slug=shop_slug)
        product = get_object_or_404(
            Product, slug=product_slug, in_stock=True, shop=shop
        )
        context = {"product": product, 'shop': shop}
        return render(request, self.template_name, context)
