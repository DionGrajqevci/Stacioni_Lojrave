from http.client import HTTPResponse
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .models import Product,Futbollisti,Skuadra
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from .models import Cart,Offer
from django.db.models import Sum,F
import stripe
from django.template.defaultfilters import floatformat
from .forms import FutbollistiForm



stripe.api_key = settings.STRIPE_SECRET_KEY




def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 9)  # Display 9 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj
    }
    return render(request, 'index.html', context)

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

def filter_products(request, product_type):
    products = Product.objects.filter(type=product_type)
    paginator = Paginator(products, 9)  # Display 9 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'product_type': product_type
    }
    return render(request, 'filtered_products.html', context)


def search_products(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)
    context = {
        'products': products,
        'query': query
    }
    return render(request, 'search_results.html', context)


def cart_view(request):
    user = request.user  # Assuming the user is authenticated
    cart_items = Cart.objects.filter(user=user)
    total_price = cart_items.annotate(
        item_total=F('product__price') * F('quantity')
    ).aggregate(sum_total=Sum('item_total'))['sum_total']
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        cart, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart.quantity += 1
            cart.save()
    
    return redirect('cart')  # Redirect to the cart page or any other appropriate page


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')


def apply_voucher(request):
    if request.method == 'POST':
        voucher_code = request.POST.get('voucher_code')

        try:
            offer = Offer.objects.get(code=voucher_code)
            discount = offer.discount
            cart_items = Cart.objects.filter(user=request.user)
            total_price = cart_items.aggregate(sum_total=Sum('product__price'))['sum_total']
            total_price_after_discount = total_price - (total_price * (discount / 100))

            context = {
                'cart_items': cart_items,
                'total_price': total_price,
                'discount': floatformat(discount, 0),  # Format the discount percentage without decimal places
                'total_price_after_discount': floatformat(total_price_after_discount, 2),  # Format the final total with 2 decimal places
            }
            return render(request, 'cart.html', context)
        except Offer.DoesNotExist:
            error_message = 'Invalid voucher code.'
            cart_items = Cart.objects.filter(user=request.user)
            total_price = cart_items.aggregate(sum_total=Sum('product__price'))['sum_total']
            context = {
                'cart_items': cart_items,
                'total_price': total_price,
                'error_message': error_message,
            }
            return render(request, 'cart.html', context)

    return render(request, 'cart.html')


def checkout(request):
    if request.method == 'POST':
        # Retrieve the payment method ID from the request
        payment_method_id = request.POST.get('payment_method_id')

        if payment_method_id:
            try:
                # Confirm the payment using the payment method ID
                # Your payment processing logic here

                # Redirect to the checkout page after successful payment
                return redirect('checkout')
            except stripe.error.CardError as e:
                # Handle card payment error
                error_message = e.error.message
                return render(request, 'checkout.html', {'error_message': error_message})
        else:
            return HttpResponse("Payment method ID not provided.")
    else:
        return render(request, 'checkout.html')


def success(request):
    return render(request, 'success.html')


def futbollisti_list(request):
    futbollistis = Futbollisti.objects.all()
    context = {'futbollistis': futbollistis}
    return render(request, 'base.html', context)

def your_view_function(request):
    futbollistis = Futbollisti.objects.all()
    context = {
        'futbollistis': futbollistis
    }
    return render(request, 'base.html', context)


def futbollisti_view(request):
    futbollistis = Futbollisti.objects.all()
    context = {
        'futbollistis': futbollistis
    }
    return render(request, 'futbollisti.html', context)

def skuadra_view(request):
    skuadras = Skuadra.objects.all()
    context = {
        'skuadras': skuadras
    }
    return render(request, 'futbollisti.html', context)


def add_futbollisti(request):
    if request.method == 'POST':
        form = FutbollistiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('futbollisti_list')
    else:
        form = FutbollistiForm()
    
    return render(request, 'futbollisti.html', {'futbollisti': Futbollisti.objects.all(), 'form': form})