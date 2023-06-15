from django.contrib import admin
from .models import Offer, Product , Futbollisti,Skuadra

class OfferAdmin(admin.ModelAdmin):
    list_display = ("code" , "discount")

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


class FutbollistiAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'team')




admin.site.register(Offer,OfferAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Skuadra)
admin.site.register(Futbollisti, FutbollistiAdmin)