from django.urls import path
from .views import fetch_wallet

urlpatterns = [
    path('', fetch_wallet, name='fetch_wallet'),
]