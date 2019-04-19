from django.shortcuts import render

def showProduct(request):
    return render(request,"product_details/product_details.html")
