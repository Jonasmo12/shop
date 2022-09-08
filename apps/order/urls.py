from django.urls import path
from .views import (
    CreateOrderView,
)


app_name = 'order'


urlpatterns = [
    path('add/', CreateOrderView.as_view(), name='add'),
]