from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from supplier.views import supplier_list, create_supplier, update_supplier, delete_supplier

urlpatterns = [
    path('', supplier_list, name='supplier_list'),
    path('create', create_supplier, name='create_supplier'),
    path('update/<int:supplier_id>/', update_supplier, name='update_supplier'),
    path('delete/<int:supplier_id>', delete_supplier, name='delete_supplier'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
