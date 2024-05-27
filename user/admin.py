from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'username', 'email', 'first_name', 'last_name']

