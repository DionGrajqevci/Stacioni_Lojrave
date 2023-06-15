from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Product(models.Model):
    PS = 'PlayStation'
    XB = 'Xbox'
    PC = 'PC'
    AC = 'Accessories'

    TYPE_CHOICES = [
        (PS, 'PlayStation'),
        (XB, 'Xbox'),
        (PC, 'PC'),
        (AC, 'Accessories'),
    ]

    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    description = models.CharField(max_length=5000)
    type = models.CharField(max_length=13, choices=TYPE_CHOICES)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


class Skuadra(models.Model):
    name = models.CharField(max_length=100)
    skuadra_id = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.name}56162"

class Futbollisti(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    team = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}56162"