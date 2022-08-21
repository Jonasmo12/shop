from django.urls import path
from .views import (
    CreateOrderView, 
    OrderConfirmation,
)


app_name = 'order'


urlpatterns = [
    path('add/', CreateOrderView.as_view(), name='add'),
    path('confirmation/', OrderConfirmation.as_view(), name='order_confirmation')
]