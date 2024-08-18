from django.shortcuts import render,redirect
from customer.models import Customer
from .forms import CustomerForm

# Create your views here.

def customer_list(request):
    form = CustomerForm()
    context = {
        "customers" : Customer.objects.all(),
        "customer_form" : form
    }
    
    return render(request, 'customer/customer_list.html', context )


def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('customer_list')  

    else:
        form = CustomerForm()

    context = {
        "customer_form": form
    }

    return render(request, 'customer/create_customer.html', context)

def delete_customer(request, customer_id):
    Customer.objects.get(id = customer_id).delete()
    return redirect('customer_list')

  # status = form.cleaned_data['status']
            # name = form.cleaned_data['name']
            # phone = form.cleaned_data['phone']
            # address = form.cleaned_data['address']
            # opening_amount = form.cleaned_data['opening_amount']
            # credit_limit = form.cleaned_data['credit_limit']
            
            # Customer.objects.create(
            #     status = status,
            #     name = name,
            #     phone = phone,
            #     address = address,
            #     opening_amount = opening_amount,
            #     credit_limit = credit_limit
            # )
           