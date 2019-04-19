from product_details.views import showProduct
from . import views
from django.urls import path

urlpatterns = [
    path('', views.showProduct, name='product_details'),

    ]