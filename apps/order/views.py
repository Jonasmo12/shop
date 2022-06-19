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
        token_id = request.POST.get('token_id')
        cart_total = str(cart.get_total_price())
        cart_total = cart_total.replace('.', '')
        cart_total = int(cart_total)

        response = requests.post(
            'https://online.yoco.com/v1/charges/',
            headers={
                'X-Auth-Secret-Key': settings.YOCO_SECRET_KEY,
            },
            json={
                'token': token_id,
                'amountInCents': cart_total,
                'currency': 'ZAR',
            },
        )
        print("--------")
        print(response.json())
        print("--------")

        # Check if order exists
        if Order.objects.filter(order_id=token_id).exists():
            pass
        else:
            order = Order.objects.create(
                order_id=token_id,
                first_name='',
                last_name='',
                address1='',
                address2='',
                post_code='',
                city='',
                phone='',
                email='',
                total_paid=cart_total,
                complete=True
            )
            order_id = order.pk

            for item in cart:
                OrderItem.objects.create(
                    order_id=order_id, 
                    product=item['product'], 
                    price=item['price'], 
                    quantity=item['quantity']
                )

        response = JsonResponse({'success': 'Return something'})
        return response


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders