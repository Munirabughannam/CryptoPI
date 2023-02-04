from django.db import models


class crypto(models.Model):
    coin_name = models.CharField(max_length=120)
    price = models.FloatField()
    hourly_change = models.CharField(max_length=120)
    daily_change = models.CharField(max_length=120)
