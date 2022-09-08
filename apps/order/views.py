from django.shortcuts import render
from django.views.generic import View
from decimal import Decimal
from django.http import JsonResponse
from ..cart.cart import Cart
from .models import Order, OrderItem
from ..shop.models import Shop
from .utils import randomOrderNumber


class CreateOrderView(View):

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            city = request.POST.get('city')
            province = request.POST.get('province')
            post_code = request.POST.get('post_code')
            shop = request.POST.get('shop')

            """
            Grap shop instance for directing the order to 
            correct shop.
            """
            shop = Shop.objects.get(name=shop) # get shop instance
            cart_total = cart.get_total_price() + Decimal(shop.shipping_fee)
            
            order = Order.objects.create(
                shop=shop,
                order_id=randomOrderNumber(),
                first_name=first_name,
                last_name=last_name,
                address1=address1,
                address2=address2,
                post_code=post_code,
                city=city,
                province=province,
                phone=phone,
                email=email,
                total_paid=cart_total,
                complete=False
            )
            
            for item in cart:
                OrderItem.objects.create(
                    order=order, 
                    product=item['product'], 
                    price=item['price'], 
                    quantity=item['quantity']
                )

            cart.clear()
            cart_quantity = cart.__len__() * 0 # set cart quantity to zero

            return JsonResponse({
                'order': order.order_id, 
                'total': order.total_paid, 
                'date': order.created.strftime("%Y-%m-%d %H:%M:%S"),
                'cart_quantity': cart_quantity
            })
        else:
            response = JsonResponse({'success': response.status_code})
            return response

