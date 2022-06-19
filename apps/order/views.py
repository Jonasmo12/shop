from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from ..cart.cart import Cart
from .models import Order, OrderItem
import requests
# Create your views here.

def add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        order_key = request.POST.get('order_key')
        token_id = request.POST.get('token_id')
        print(order_key)
        # cart_total = cart.get_total_price()
        total = str(cart.get_total_price())
        total = total.replace('.', '')
        total = int(total)

        response = requests.post(
            'https://online.yoco.com/v1/charges/',
            headers={
                'X-Auth-Secret-Key': settings.YOCO_SECRET_KEY,
            },
            json={
                'token': token_id,
                'amountInCents': total,
                'currency': 'ZAR',
            },
        )
        print("--------")
        print(response.json())
        print("--------")

        # # Check if order exists
        # if Order.objects.filter(order_key=order_key).exists():
        #     pass
        # else:
        #     order = Order.objects.create()
        #     order_id = order.pk

        #     for item in cart:
        #         OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

        response = JsonResponse({'success': 'Return something'})
        return response


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders