from django.shortcuts import render
from .models import Product


def home(request):
    product_list = Product.objects.all()
    return render(request, "home/home.html",{'product_list':product_list})

