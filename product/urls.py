from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from product.views import product_list, product_create, product_update, product_delete

urlpatterns = [
    path('', product_list, name='product_list'),
    path('create', product_create, name='product_create'),
    path('update/<int:product_id>/', product_update, name='product_update'),
    path('delete/<int:product_id>', product_delete, name='product_delete'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
