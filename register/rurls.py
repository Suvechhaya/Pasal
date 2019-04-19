from register.views import registerForm
from . import views
from django.urls import path

urlpatterns = [
    path('', views.loginForm, name='login'),
    path('register/', views.registerForm, name='register')


]