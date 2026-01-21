from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin

admin.site.register(CustomUser, CustomUserAdmin)
