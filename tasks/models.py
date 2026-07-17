from django.conf import settings
from django.db import models

from employees.models import Employee


class Task(models.Model):
    """
    Task model.
    """

    class Priority(models.TextChoices):
        LOW = "LOW", "Low"
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"
        CRITICAL = "CRITICAL", "Critical"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        REVIEW = "REVIEW", "Under Review"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField()

    assigned_to = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="assigned_tasks",
    )

    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    progress = models.PositiveSmallIntegerField(
        default=0,
        help_text="Progress percentage (0-100).",
    )

    start_date = models.DateField()

    due_date = models.DateField()

    completed_date = models.DateField(
        blank=True,
        null=True,
    )

    remarks = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]

    @property
    def is_overdue(self):
        from django.utils import timezone

        return (
            self.status != self.Status.COMPLETED
            and self.due_date < timezone.now().date()
        )

    def __str__(self):
        return self.title