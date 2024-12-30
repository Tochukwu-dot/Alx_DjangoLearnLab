from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .models import CustomUser

# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Imporant dates', {'fields': ('last_login', 'date_joined')}),
#     )

# admin.site.register(CustomUser, CustomUserAdmin)