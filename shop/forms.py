from django import forms
from django.core.exceptions import ValidationError

from shop.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'remainder', 'cost')


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label="Search")


