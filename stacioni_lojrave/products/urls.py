from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("new", views.new),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]

