from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),      
    path('<int:product_id>/update_review/<int:review_id>', views.update_review, name="update_review"), 
    path('delete_review/<str:pk>/', views.delete_review, name="delete_review"), 
]