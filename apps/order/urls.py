from django.urls import path
from .views import add

app_name = 'order'

urlpatterns = [
    path('add/', add, name='add'),
]