from django.shortcuts import render, get_object_or_404
from decimal import Decimal
from ..cart.cart import Cart
from ..shop.models import Shop


def CartView(request, shop_slug=None):
    cart = Cart(request)
    shop = get_object_or_404(Shop, active=True, slug=shop_slug)
    cart_total = cart.get_subtotal_of_product() + Decimal(shop.shipping_fee)
    context = {
        'shop': shop, 
        'cart_total': cart_total
    }
    return render(request, 'payment/payment.html', context)
