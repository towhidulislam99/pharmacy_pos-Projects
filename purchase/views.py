from django.shortcuts import render
from purchase.forms import SelectProductForm

def parchase_product(request):
    prouct_form =SelectProductForm()
    
    context = {
        "product_form" : prouct_form
    }
    
    return render(request, 'purchase/purchase_product.html', context )
