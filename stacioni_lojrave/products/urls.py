from django.urls import path
from . import views
from .views import add_to_cart
from .views import cart_view,remove_from_cart,futbollisti_list,add_futbollisti

urlpatterns = [
    path("", views.index),
    path("new", views.new),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/<str:product_type>/', views.filter_products, name='filter_products'),
    path('search/', views.search_products, name='search_products'),
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('apply-voucher/', views.apply_voucher, name='apply_voucher'),
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.success, name='success'),
    path('futbollistis/', futbollisti_list, name='futbollisti_list'),
    path('futbollisti/', views.futbollisti_view, name='futbollisti'),
    path('futbollisti/add/', add_futbollisti, name='add_futbollisti'),
]

