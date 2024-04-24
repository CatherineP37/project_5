from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm, Review


# Create your views here.

def products(request):
    """ A view to show products and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria.")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)




def product_detail(request, product_id):
    """ A view to show individual product details """
    reviews = Review.objects.all()    
    product = get_object_or_404(Product, pk=product_id)
    
    context = {
        'product': product,
        'reviews': reviews,
             
    }

    return render(request, 'products/product_detail.html', context)

    def __str__(self):
        return self.review.title

def create_review(request):
    form = createReview()
    if request.method == 'POST':
        form = Reviews(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')   
    
    context = {       
        'form': form        
    }

    return render(request, 'products/product_detail.html', context)

def update_review(request, pk):

    review = Review.objects.get(id=pk)
    form = createReview(instance=review)

    if request.method == 'POST':
        form = createReview(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('/')
               

    context = {'form':form}
    return render(request, 'products/update_review.html', context)
    def __str__(self):
        return self.name

def delete_review(request, pk):
    review = Review.objects.get(id=pk)
    if request.method == "POST":
        review.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'products/delete_review.html', context)

   







        
       