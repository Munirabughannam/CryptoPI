from django.shortcuts import render
from rest_framework import generics
from django.http import response
from .models import crypto
from .serializers import cryptoserializer

class CoinView(generics.ListAPIView):
    queryset = crypto.objects.all()
    serializer_class = cryptoserializer




