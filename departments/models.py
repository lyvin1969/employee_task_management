from django.db import models
from django.conf import settings


class Department(models.Model):
    """
    Stores department information.
    """

    department_name = models.CharField(
        max_length=100,
        unique=True,
    )

    department_code = models.CharField(
        max_length=20,
        unique=True,
    )

    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_departments",
    )

    email = models.EmailField(
        blank=True,
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
    )

    location = models.CharField(
        max_length=150,
        blank=True,
    )

    description = models.TextField(
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
        ordering = ["department_name"]
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return f"{self.department_name} ({self.department_code})"