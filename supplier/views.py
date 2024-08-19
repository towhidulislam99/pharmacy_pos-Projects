from django.shortcuts import render, redirect, get_object_or_404
from supplier.models import Supplier
from .forms import SupplierForm



def supplier_list(request):
    form = SupplierForm()
    context = {
        "suppliers": Supplier.objects.all(),
        "supplier_form": form
    }

    return render(request, 'supplier/supplier_list.html', context)


def create_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')  # Ensure this URL name exists

    else:
        form = SupplierForm()

    context = {
        "supplier_form": form
    }

    return render(request, 'supplier/create_supplier.html', context)


def update_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')  # Redirect to the supplier list after updating
    else:
        form = SupplierForm(instance=supplier)

    context = {
        "supplier_form": form,
        "supplier": supplier
    }

    return render(request, 'supplier/update_supplier.html', context)



def delete_supplier(request, supplier_id):
    Supplier.objects.get(id = supplier_id ).delete()
    return redirect('supplier_list')


# manufectural = form.cleaned_data['is_manufectural']
            # name = form.cleaned_data['supplier_name']
            # phone = form.cleaned_data['supplier_phone']

            # Supplier.objects.create(
            #     is_manufactural=manufectural,
            #     supplier_name=name,
            #     supplier_phone=phone
            # )