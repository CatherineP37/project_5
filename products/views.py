from django.shortcuts import render
from .models import Product

# Create your views here.

def full_collection(request):
    """ A view to show full collection, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/full_collection.html', context)
