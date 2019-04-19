"""pasal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.categories, name='categories')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='categories')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#from categories import hurls
from product_details import purls
from register import rurls
from pasal import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/',include("categories.hurls")),
    path('product_details/',include(purls)),
    path('register/',include("register.rurls")),
    path('contact/',include("contact.curls")),
    path('home/',include("home.hourls")),
    path('cart/',include("cart.caurls"))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

