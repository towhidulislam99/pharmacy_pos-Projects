from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from user_account.views import register, login_view, user_list, update_user, delete_user

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('users', user_list, name='user_list'),
    path('user/update/<int:user_id>/', update_user, name='update_user'),
    path('user/delete/<int:user_id>/', delete_user, name='delete_user'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
