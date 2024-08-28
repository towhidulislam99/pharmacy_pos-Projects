from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from customer.views import customer_list,create_customer, update_customer, delete_customer

urlpatterns = [
    path('', customer_list, name='customer_list'),
    path('create', create_customer, name='create_customer'),
    path('update/<int:customer_id>/', update_customer, name='update_customer'),
    path('delete/<int:customer_id>', delete_customer, name='delete_customer'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
