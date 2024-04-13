from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def contact(request):
    """ A view to return the contact page """
    
    context = {}
    form = Contact()
    
    if request.method == 'POST':
        form = Contact(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user            
            instance.save()
            return redirect('contact')            
    
    return render(request, 'home/contact.html')

def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')

def privacy(request):
    """ A view to return the privacy page """

    return render(request, 'home/privacy.html')

def account(request):
    """ A view to return the account page """

    return render(request, 'home/account.html')

def sitemap(request):
    """ A view to return the sitemap page """

    return render(request, 'home/sitemap.html')