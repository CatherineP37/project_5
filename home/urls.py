from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
    path('privacy/',views.account, name="privacy"),
    path('about/', views.booking, name="about"),
    path('contact/', views.booking, name="contact"),
]