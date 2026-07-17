from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Admin configuration for Employee model.
    """

    list_display = (
        "employee_number",
        "get_full_name",
        "job_title",
        "phone_number",
        "status",
        "hire_date",
    )

    list_filter = (
        "status",
        "gender",
        "hire_date",
    )

    search_fields = (
        "employee_number",
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
        "national_id",
        "phone_number",
    )

    ordering = (
        "employee_number",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "User Information",
            {
                "fields": (
                    "user",
                    "employee_number",
                    "job_title",
                    "status",
                )
            },
        ),
        (
            "Personal Information",
            {
                "fields": (
                    "gender",
                    "date_of_birth",
                    "national_id",
                    "phone_number",
                    "address",
                    "profile_photo",
                )
            },
        ),
        (
            "Employment Information",
            {
                "fields": (
                    "hire_date",
                )
            },
        ),
        (
            "Emergency Contact",
            {
                "fields": (
                    "emergency_contact_name",
                    "emergency_contact_phone",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    def get_full_name(self, obj):
        return obj.user.get_full_name() or obj.user.username

    get_full_name.short_description = "Employee Name"