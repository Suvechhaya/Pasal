from django.shortcuts import render
from .models import Product


def categories(request):
    product_list = Product.objects.all()
    return render(request, "categories/categories.html",{'product_list':product_list , 'latest':product_list[0]})

