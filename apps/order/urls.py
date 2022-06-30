from django.urls import path
from .views import add, OrderConfirmation

app_name = 'order'

urlpatterns = [
    path('add/', add, name='add'),
    path('confirmation/', OrderConfirmation.as_view(), name='order_confirmation')
]