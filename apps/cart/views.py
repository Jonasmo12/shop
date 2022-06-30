from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from ..shop.models import Shop
from ..product.models import Product
from .cart import Cart


def cart_summary(request, shop_slug=None):
    cart = Cart(request)
    shop = get_object_or_404(Shop, active=True, slug=shop_slug)
    return render(request, 'shop/cart.html', {'cart': cart, 'shop': shop})


def cart_add(request, shop_slug=None):
    cart = Cart(request)
    shop = get_object_or_404(Shop, active=True, slug=shop_slug)
    print(request.POST.get('csrfmiddlewaretoken'))
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_quantity)

        cart_quantity = cart.__len__()
        response = JsonResponse({'quantity': cart_quantity})
        print(response)
        return response


def cart_delete(request, shop_slug=None):
    cart = Cart(request)
    shop = get_object_or_404(Shop, active=True, slug=shop_slug)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)

        cart_quantity = cart.__len__()
        cart_total = cart.get_total_price()
        response = JsonResponse({'cart_quantity': cart_quantity, 'subtotal': cart_total})
        return response


def cart_update(request, shop_slug=None):
    cart = Cart(request)
    shop = get_object_or_404(Shop, active=True, slug=shop_slug)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        cart.update(product=product_id, quantity=product_quantity)
        
        qs = cart.get_subtotal_of_product()
        print(qs)
        cart_quantity = cart.__len__()
        cart_subtotal = cart.get_subtotal_price()
        cart_total_price = cart.get_total_price()
        response = JsonResponse({
            'cart_quantity': cart_quantity, 
            'subtotal': cart_subtotal,
            'total_price': cart_total_price
        })
        print(response)
        return response
