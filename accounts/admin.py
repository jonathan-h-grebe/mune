from django.contrib import admin

# Register your models here.
from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin 
from django.utils.translation import gettext_lazy as _ 
from .models import CustomUser 


class CustomUserAdmin(UserAdmin): 
    fieldsets = ( 
            (None, {'fields': ('username', 'password')}), 
            #個 ⼈ 情 報 欄 に 'age' を 追加 
            (_('Personal info'), {
                'fields': (
                    'first_name', 'last_name', 'email', 'age',
                    "tel_number"
                )
                }),
            (_('Company info'), {
                'fields': ('company_name', 'company_address')
            }),
            (_('Permissions'), {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
                }), 
            (_('Important dates'), {
                'fields': ('last_login', 'date_joined')
                }), 
            ) 

admin.site.register(CustomUser, CustomUserAdmin)

