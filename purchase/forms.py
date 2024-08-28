from django import forms
from product.models import Product

class SelectProductForm(forms.Form):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',  # Bootstrap class for styling
            'placeholder': 'Select a product',
        })
    )