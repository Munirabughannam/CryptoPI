from rest_framework import generics
from .models import crypto
from .serializers import cryptoserializer



class CoinView(generics.ListAPIView):
    queryset = crypto.objects.all()
    serializer_class = cryptoserializer
    ordering_fields = ['price']
    search_fields = ['coin_name']




