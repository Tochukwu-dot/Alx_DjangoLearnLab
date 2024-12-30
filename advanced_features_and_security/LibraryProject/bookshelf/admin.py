from django.contrib import admin
from .models import Book
# Register your models here.
class BookAdmin (admin.ModelAdmin):
    list_display = ('author', 'title', 'publication_year')
    list_filter = ('author', 'title', 'publication_year')
    search_fields = ('author', 'title', 'publication_year')


admin.site.register (Book, BookAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

