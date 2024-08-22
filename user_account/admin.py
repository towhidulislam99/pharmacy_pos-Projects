from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class CustomUserAdmin(BaseUserAdmin):
    # Define the fields to be used in displaying the User model in the admin interface
    list_display = ('username', 'email', 'status', 'role', 'gender', 'phone', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)

    # Define the layout of the user edit form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'status', 'role', 'gender', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Define the layout of the add user form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'status', 'role', 'gender', 'phone', 'password1', 'password2'),
        }),
    )

    # Define form used for creating a user
    def save_model(self, request, obj, form, change):
        if not change:  # If adding a new user
            obj.set_password(form.cleaned_data['password1'])
        super().save_model(request, obj, form, change)

# Register the custom admin class with the User model
admin.site.register(User, CustomUserAdmin)








# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# class CustomUserAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('status', 'role', 'gender', 'phone')}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('status', 'role', 'gender', 'phone')}),
#     )

# admin.site.register(User, CustomUserAdmin)
