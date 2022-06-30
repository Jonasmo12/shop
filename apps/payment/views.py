from django.shortcuts import render, get_object_or_404
from ..cart.cart import Cart
from ..shop.models import Shop


def CartView(request, shop_slug=None):
    cart = Cart(request)
    shop = get_object_or_404(Shop, active=True, slug=shop_slug)
    context = {'shop': shop}
    print(shop)
    return render(request, 'payment/payment.html', context)
