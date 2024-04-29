from django import forms
from django.forms import ModelForm
from .widgets import CustomClearableFileInput
from .models import Product, Review

class createReview(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user',)
        widgets={
            'title' : forms.TextInput(attrs={'style': "width:100%;"}),            
            'review' : forms.Textarea(attrs={'style': "width:100%;"}),
        }
      