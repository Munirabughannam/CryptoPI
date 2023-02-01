from rest_framework import serializers
from .models import crypto

class cryptoserializer(serializers.ModelSerializer):
    class Meta:
        model = crypto
        fields = '__all__'