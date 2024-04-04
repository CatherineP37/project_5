from django.urls import path
from . import views

urlpatterns = [
    path('', views.full_collection, name='full_collection'),
    path('<product_id>', views.product_detail, name='product_detail'),
]