from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User

    fieldsets = (
        (None, {"fields": ("email", "password", "full_name")}),
        ("Permission", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2"),}),
    )

    filter_horizontal = ()
    ordering = ("email", "full_name")
    list_filter = ("email", "full_name")
    list_display = ("pk", "email", "full_name")
