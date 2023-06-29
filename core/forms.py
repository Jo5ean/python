from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100)
