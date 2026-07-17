from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Admin configuration for the Custom User model.
    """

    # Fields displayed in the user list
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "role",
        "is_staff",
        "is_active",
        "date_joined",
    )

    # Filters in the right sidebar
    list_filter = (
        "role",
        "is_staff",
        "is_superuser",
        "is_active",
        "groups",
    )

    # Search functionality
    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
    )

    # Default ordering
    ordering = (
        "first_name",
        "last_name",
    )

    # Read-only fields
    readonly_fields = (
        "last_login",
        "date_joined",
        "created_at",
        "updated_at",
    )

    # Organize fields when editing a user
    fieldsets = (
        ("Login Information", {
            "fields": (
                "username",
                "password",
            )
        }),

        ("Personal Information", {
            "fields": (
                "first_name",
                "last_name",
                "email",
                "phone",
                "profile_picture",
            )
        }),

        ("Role & Permissions", {
            "fields": (
                "role",
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),

        ("Important Dates", {
            "fields": (
                "last_login",
                "date_joined",
                "created_at",
                "updated_at",
            )
        }),
    )

    # Fields shown when adding a new user
    add_fieldsets = (
        (
            "Create New User",
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "role",
                    "profile_picture",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )