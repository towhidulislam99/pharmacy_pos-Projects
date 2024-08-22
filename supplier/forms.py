from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        widgets = {
            'is_manufactural': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'supplier_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter supplier name'}),
            'supplier_phone': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter phone number'}),
        }
