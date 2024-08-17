from django import forms
from .models import Customer
 
class CustomerForm(forms.Form):
    STATUS_CHOICES = Customer.STATUS_CHOICES  # Use the choices from the model
    
    status = forms.ChoiceField(choices=STATUS_CHOICES)  # Use ChoiceField for dropdown
    name = forms.CharField()  
    phone = forms.CharField() 
    address = forms.CharField(widget=forms.Textarea)
    opening_amount = forms.DecimalField()  
    credit_limit = forms.DecimalField() 