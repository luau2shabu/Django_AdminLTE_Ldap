from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('gid','name','email','department','role','l','startdate', 'is_staff', 'is_active',)
    list_filter = ('gid','name','email','department','role','l','startdate', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('gid','name','email','department','role','l','startdate', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('gid', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('gid',)
    ordering = ('gid',)


admin.site.register(CustomUser, CustomUserAdmin)