"""
URL configuration for pharmacy_pos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.conf import settings
from supplier.views import supplier_list, create_supplier, update_supplier, delete_supplier
from customer.views import customer_list,create_customer, update_customer, delete_customer
from user_account.views import register, login_view, user_list, update_user, delete_user


def dashboard(request):
    return render(request, 'dashboard.html')


urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('users', user_list, name='user_list'),
    path('user/update/<int:user_id>/', update_user, name='update_user'),
    path('user/delete/<int:user_id>/', delete_user, name='delete_user'),
    
    path('dashboard', dashboard, name='home'),
    
    path('suppliers', supplier_list, name='supplier_list'),
    path('suppliers/create', create_supplier, name='create_supplier'),
    path('suppliers/update/<int:supplier_id>/', update_supplier, name='update_supplier'),
    path('suppliers/delete/<int:supplier_id>', delete_supplier, name='delete_supplier'),
    
    path('customer', customer_list, name='customer_list'),
    path('customer/create', create_customer, name='create_customer'),
    path('customer/update/<int:customer_id>/', update_customer, name='update_customer'),
    path('customer/delete/<int:customer_id>', delete_customer, name='delete_customer'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
