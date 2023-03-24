from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile
from .forms import CustomUserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)