from django.shortcuts import render, redirect, get_object_or_404, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_account/register.html', {'register_form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a success page.
            else:
                form.add_error(None, "Invalid username or password.")
        else:
            form.add_error(None, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'user_account/login.html', {'login_form': form})


User = get_user_model()  # Use the custom user model
def user_list(request):
    users = User.objects.all()  # Retrieve all user records
    context = {
        'users': users
    }
    return render(request, 'user_account/users_list.html', context)


def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            
            if password1:
                user.set_password(password1)
            user.save()
            update_session_auth_hash(request, user)  # Keeps the user logged in after password change
            return redirect('user_list')  # Redirect to a user list or another appropriate page
    else:
        form = CustomUserUpdateForm(instance=user)

    return render(request, 'user_account/update_user.html', {'update_user': form})


@login_required
@user_passes_test(lambda u: u.is_superuser)  # Ensure that only superusers can delete users
# def delete_user(request, user_id):
#     user = get_object_or_404(User, id=user_id)

#     if request.method == 'POST':
#         user.delete()
#         return redirect('user_list')  # Redirect to a user list or another page after deletion

#     return render(request, 'user_account/confirm_delete.html', {'user': user})

def delete_user(request, user_id):
    User.objects.get(id = user_id).delete()
    return redirect('user_list')