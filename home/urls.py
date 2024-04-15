from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('privacy/',views.privacy, name="privacy"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('events/', views.contact, name="events"),
    path('sitemap/', views.contact, name="sitemap"),
]