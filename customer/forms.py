from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter supplier name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter address'}),
            'opening_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter opening amount'}),
            'credit_limit': forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter credit limit'}),
        }  