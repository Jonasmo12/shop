from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import View, TemplateView
from .models import Shop


class HomeView(TemplateView):
    template_name = 'home.html'


class ShopView(View):
    template_name = 'shop/shop.html'
    model = Shop
    queryset = Shop.objects.all()
    context_object_name = 'shop'

    def get(self, request, shop_slug, *args, **kwargs):
        shop = get_object_or_404(Shop, slug=shop_slug)
        products = shop.product_set.all()
        paginator = Paginator(products, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'shop': shop, 'products': products, 'page_obj': page_obj}
        return render(request, self.template_name, context)

    