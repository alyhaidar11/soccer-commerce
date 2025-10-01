from django.forms import ModelForm
from main.models import Product
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name","price","quantity","description","thumbnail","category","is_featured"]
        widgets = {
            'price': forms.NumberInput(attrs={'step': 100000}),
        }