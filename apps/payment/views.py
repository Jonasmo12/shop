import json
from django.conf import settings
import requests
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from ..cart.cart import Cart
from ..order.views import payment_confirmation


def order_placed(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'payment/payment_confirmation.html')


class Error(TemplateView):
    template_name = 'payment/payment_error.html'



def CartView(request):

    cart = Cart(request)
    total = str(cart.get_total_price())
    total = total.replace('.', '')
    total = int(total)
    print('1-------2')
    print(total)

    if request.method == 'POST':
        response = requests.POST(
            'https://online.yoco.com/v1/charges/',
            headers={
                'X-Auth-Secret-Key': settings.YOCO_SECRET_KEY,
            },
            json={
                'token': 'tok_test_DjaqoUgmzwYkwesr3euMxyUV4g',
                'amountInCents': total,
                'currency': 'ZAR',
            },
        )
        print("--------")
        print(response.json())
        print("--------")
        return JsonResponse({'response': response})
    print(123)
    return render(request, 'payment/payment.html')


# @csrf_exempt
# def stripe_webhook(request):
#     # payload = request.body
#     # event = None

#     # try:
#     #     event = stripe.Event.construct_from(
#     #         json.loads(payload), stripe.api_key
#     #     )
#     # except ValueError as e:
#     #     print(e)
#     #     return HttpResponse(status=400)

#     # # Handle the event
#     # if event.type == 'payment_intent.succeeded':
#     #     payment_confirmation(event.data.object.client_secret)

#     # else:
#     #     print('Unhandled event type {}'.format(event.type))

#     return HttpResponse(status=200)