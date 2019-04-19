from contact.views import Contact
from . import views
from django.urls import path

urlpatterns = [
    path('', views.contactForm, name='contact'),

    ]
