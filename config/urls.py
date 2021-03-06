from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    # path('cart/', include('apps.cart.urls')),
    path('order/', include('apps.order.urls', namespace='order')),
    # path('payment/', include('apps.payment.urls', namespace='payment')),
    path('', include('apps.shop.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)