from django import forms
from django.forms import ModelForm
from .models import Contact


class BookAppointment(ModelForm):
    class Meta:
        model = Contact
      