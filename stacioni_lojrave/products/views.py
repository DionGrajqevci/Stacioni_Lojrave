from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404


def index(request):
    products = Product.objects.all()
    return render(request,"index.html",{"products": products})


def new(request):
    return HttpResponse("New Products")

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)