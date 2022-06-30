from django.urls import path, include
from .views import (
    ShopView,
    HomeView
)

app_name = "shop"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<str:shop_slug>/', ShopView.as_view(), name='shop'),
    path('<str:shop_slug>/cart/', include('apps.cart.urls', namespace='cart')),
    path('<str:shop_slug>/payment/', include('apps.payment.urls', namespace='payment')),
    path('<str:shop_slug>/', include('apps.product.urls', namespace="product")),
]
