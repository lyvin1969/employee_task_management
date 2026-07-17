from django.contrib import admin

from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """
    Admin configuration for Department model.
    """

    list_display = (
        "department_name",
        "department_code",
        "manager",
        "email",
        "phone_number",
        "location",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "department_name",
        "department_code",
        "manager__username",
        "manager__first_name",
        "manager__last_name",
    )

    ordering = (
        "department_name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Department Information",
            {
                "fields": (
                    "department_name",
                    "department_code",
                    "manager",
                ),
            },
        ),

        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone_number",
                    "location",
                ),
            },
        ),

        (
            "Additional Information",
            {
                "fields": (
                    "description",
                    "is_active",
                ),
            },
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),

    )
