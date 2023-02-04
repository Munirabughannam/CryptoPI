from django.urls import path
from .views import CoinView

urlpatterns = [
    path('', CoinView.as_view())
]