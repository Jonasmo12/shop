from django.urls import path, include
from .views import ShopView

app_name = "shop"

urlpatterns = [
    path('<str:shop_slug>/', ShopView.as_view(), name='shop'),
    path('<str:shop_slug>/', include('apps.product.urls', namespace="product")),
]
