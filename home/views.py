from django.shortcuts import render
from .forms import ContactForm, AttendanceForm
from .models import Event
from django.contrib import messages

# Create your views here.

def index(request):
    """ A view to return the index page """
    messages.success(request, ('Your review has been deleted.'))
    return render(request, 'home/index.html')


def contact(request):

	form = ContactForm()

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'home/contact.html', context)


def events(request):
    
    events = Event.objects.all() 
    form = AttendanceForm()

    if request.method == 'POST':
	    form = AttendanceForm(request.POST)
	    if form.is_valid():
		    form.save()
			
    context = {'form':form,
               'events':events,
              }
    return render(request, 'home/events.html', context)



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