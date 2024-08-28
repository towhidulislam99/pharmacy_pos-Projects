from django.shortcuts import render, redirect, get_list_or_404,get_object_or_404
from product.forms import ProductForm
from product.models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products} )

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()  # This should be outside the 'if' block

    return render(request, 'product/create_product.html', {'product_form': form})

def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  
    else:
        form = ProductForm(instance=product)  

    return render(request, 'product/product_update.html', {'product_update': form})


def product_delete(request, product_id):
    Product.objects.get(id = product_id ).delete()
    return redirect('product_list')
            
