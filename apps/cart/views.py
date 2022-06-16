from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from ..product.models import Product

from .cart import Cart


def cart_summary(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart})


def cart_add(request):
    cart = Cart(request)
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


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)

        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()
        response = JsonResponse({'qty': cart_qty, 'subtotal': cart_total})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        cart.update(product=product_id, quantity=product_quantity)

        cart_quantity = cart.__len__()
        cart_total = cart.get_total_price()
        response = JsonResponse({'cart_quantity': cart_quantity, 'subtotal': cart_total})
        print(response)
        return response
