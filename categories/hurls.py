from categories.views import categories
from . import views
from django.urls import path

urlpatterns = [
    path('', views.categories, name='categories'),

    ]