from django import forms
from django.forms import ModelForm
from .widgets import CustomClearableFileInput
from .models import Product, Review

class createReview(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user')
      