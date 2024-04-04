from django.urls import path
from . import views

urlpatterns = [
    path('', views.full_collection, name='products')
]