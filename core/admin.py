from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        'username',
        'email',
        'first_name',
        'is_superuser',
        'last_name',
    ]

    list_filter = ('is_superuser',)
    
    fieldsets =  (
        ('None', {'fields': ('email',
                             'username',
                             'password')}),
        ('Personal information', {'fields': (
                                       'first_name', 
                                       'last_name')}),
        ('Permissions', {'fields': ('is_superuser', )})
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2'
            )}
         ),
    )
    
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


