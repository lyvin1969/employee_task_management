from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    """
    Custom User Model for the Employee Task Management System.
    """

    # ==========================
    # User Roles
    # ==========================
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    EMPLOYEE = "EMPLOYEE"

    ROLE_CHOICES = [
        (ADMIN, "Administrator"),
        (MANAGER, "Manager"),
        (EMPLOYEE, "Employee"),
    ]

    # ==========================
    # Additional Fields
    # ==========================
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=EMPLOYEE,
        help_text="Determines the user's access level."
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="User's phone number."
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # ==========================
    # Meta Information
    # ==========================
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["first_name", "last_name", "username"]

    # ==========================
    # String Representation
    # ==========================
    def __str__(self):
        full_name = self.get_full_name()
        return full_name if full_name else self.username

    # ==========================
    # Helper Properties
    # ==========================
    @property
    def full_name(self):
        return self.get_full_name()

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_manager(self):
        return self.role == self.MANAGER

    @property
    def is_employee(self):
        return self.role == self.EMPLOYEE