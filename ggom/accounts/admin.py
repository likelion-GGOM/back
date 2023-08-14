from django.contrib import admin
from .models import CustomUser, CustomUserManager

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'password',
        'email',
        'nickname',
        'is_active',
        'is_staff',
        'is_superuser',
    )
