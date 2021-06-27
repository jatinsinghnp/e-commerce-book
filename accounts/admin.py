
from django.contrib.auth.models import Group

from django.contrib import admin
from django.contrib.auth import models
from .models import ShopUser
from django.contrib.auth.admin import UserAdmin
from .forms import ShopCreationForm,ShopUserChangeForm
# Register your models here.


class ShopUserAdmin(UserAdmin):
    add_form=ShopCreationForm
    form=ShopUserChangeForm
    model=ShopUser
    list_display=('email', 'is_staff', 'is_active')
    list_filter=('is_admin'),
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)

    
    

admin.site.register(ShopUser,ShopUserAdmin)

admin.site.unregister(Group)
