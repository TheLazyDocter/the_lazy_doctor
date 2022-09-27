# django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# local
from .models import User, PatientProfile


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {
            "fields": ("username", "password", "kind")
        }),
        ("Personal info", {
            "fields": ("first_name", "last_name", "email")
        }),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {
            "fields": ("last_login", "date_joined")
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(PatientProfile)
