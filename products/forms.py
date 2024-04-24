from django import forms
from django.forms import ModelForm
from .widgets import CustomClearableFileInput
from .models import Product, Review



class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class createReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
      