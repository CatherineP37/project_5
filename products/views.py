from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect
from .models import Product, Review
from .forms import createReview

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
    
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)  
    form = createReview()

    if request.method == 'POST':
        form = createReview(request.POST)
        reviews = Review.objects.all()
  
        if form.is_valid():
            form.instance.product = product
            form.instance.author = request.user           
            
            form.save()
            messages.success(request, ('Thanks for your review!'))
            return redirect('product_detail', product_id=product_id)  
    
    context = {
        'product': product,
        'reviews': reviews,
        'form' : form,       
             
    }

    return render(request, 'products/product_detail.html', context)   

def update_review(request, review_id):
    """
    view to edit review
    """
    review = get_object_or_404(Review, pk=review_id)
    form = createReview(instance=review)
    product = review.product
    

    if request.method == "POST":
        form = createReview(request.POST, instance=review)            

        if form.is_valid() and review.author == request.user:
            review = form.save(commit=False)
            # review.product = product             
            review.author = request.user          
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review updated!')
            return redirect('product_detail', product_id=product.id) 
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review.')
            return redirect('update_review',) 
            
    context = {'form':form}
    return render(request, 'products/update_review.html', context) 

        

def delete_review(request, pk):
    """
    view to delete review
    """
    if request.method == "POST":
        product = get_object_or_404
        review = Review.objects.get(id=pk)

        if review.author == request.user:
            review.delete()
            messages.add_message(request, messages.SUCCESS, 'Review deleted!')
        else:
            messages.add_message(request, messages.ERROR, 'You can only delete your own reviews.')

        return HttpResponseRedirect(reverse('products/delete_review.html',))


   







        
       