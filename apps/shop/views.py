from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView
from .models import Shop

# Create your views here.

class ShopView(View):
    template_name = 'shop/shop.html'
    model = Shop
    queryset = Shop.objects.all()
    context_object_name = 'shop'

    def get(self, request, shop_slug, *args, **kwargs):
        shop = get_object_or_404(Shop, slug=shop_slug)
        products = shop.product_set.all()
        print(products)
        context = {'shop': shop, 'products': products}
        return render(request, self.template_name, context)

    