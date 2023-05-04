from django.db import models


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
    type = models.CharField(max_length=13, choices=TYPE_CHOICES)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()