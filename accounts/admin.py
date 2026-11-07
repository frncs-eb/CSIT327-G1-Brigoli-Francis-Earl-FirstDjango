from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'last_name',
        'first_name',
        'username',
        'email',
        'role',
        'is_staff',
    )

    list_filter = (
        'is_staff',
        'is_superuser',
        'is_active',
    )

    search_fields = (
        'last_name',
        'first_name',
        'username',
        'email',
    )

    ordering = ('username',)
