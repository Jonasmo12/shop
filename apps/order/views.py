from django.shortcuts import render
from django.views.generic import View
import requests
from django.conf import settings
from django.http import JsonResponse
from ..cart.cart import Cart
from .models import Order, OrderItem
from ..shop.models import Shop


def add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        token_id = request.POST.get('token_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        province = request.POST.get('province')
        zip_code = request.POST.get('post_code')
        shop = request.POST.get('shop')
        shop = Shop.objects.get(name=shop) # get shop instance
        
        """
        remove comma from price
        payment menchant wont be able to process the payment
        if there is a comma in the ammount 
        """
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
                'description': str(shop.name + '* R' + str(cart_total))
            },
        )
        
        if response.status_code == 201:
            # Check if order exists
            if Order.objects.filter(order_id=token_id).exists():
                return JsonResponse({'order_status': 'Order already Exists'})

            else:
                order = Order.objects.create(
                    shop=shop,
                    order_id=token_id,
                    first_name=first_name,
                    last_name=last_name,
                    address1=address1,
                    address2=address2,
                    post_code=zip_code,
                    city=city,
                    province=province,
                    phone=phone,
                    email=email,
                    total_paid=cart.get_total_price(),
                    complete=True
                )
                order_id = order

                for item in cart:
                    OrderItem.objects.create(
                        order=order_id, 
                        product=item['product'], 
                        price=item['price'], 
                        quantity=item['quantity']
                    )

            return JsonResponse({'success': 'order created successfully'})
        else:
            response = JsonResponse({'success': response.status_code})
            return response


class OrderConfirmation(View):
    template_name = 'payment/payment_confirmation.html'

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()
        return render(request, self.template_name)
