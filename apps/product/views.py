from math import prod
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import View
from .models import Product, Tag
from ..shop.models import Shop


class ProductDetailView(View):
    model = Product
    template_name = "product/product.html"
    
    def get(self, request, shop_slug, product_slug):
        shop = Shop.objects.get(slug=shop_slug)
        product = get_object_or_404(
            Product, slug=product_slug, in_stock=True, shop=shop
        )
        # filters objects by tag name, and excludes opened product from alike products
        tag = Product.objects.filter(tag__name=product.tag).exclude(title=product.title)
        paginator = Paginator(tag, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'product': product, 
            'shop': shop, 
            'page_obj': page_obj
        }
        return render(request, self.template_name, context)
