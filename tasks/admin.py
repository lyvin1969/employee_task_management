from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin configuration for Task model.
    """

    list_display = (
        "title",
        "assigned_to",
        "assigned_by",
        "priority",
        "status",
        "start_date",
        "due_date",
        "created_at",
    )

    list_filter = (
        "priority",
        "status",
        "start_date",
        "due_date",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "assigned_to__first_name",
        "assigned_to__last_name",
        "assigned_by__username",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Task Information",
            {
                "fields": (
                    "title",
                    "description",
                ),
            },
        ),

        (
            "Assignment",
            {
                "fields": (
                    "assigned_to",
                    "assigned_by",
                ),
            },
        ),

        (
            "Task Status",
            {
                "fields": (
                    "priority",
                    "status",
                    "remarks",
                ),
            },
        ),

        (
            "Dates",
            {
                "fields": (
                    "start_date",
                    "due_date",
                    "completed_date",
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