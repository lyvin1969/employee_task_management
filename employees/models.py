from django.db import models
from django.conf import settings
from departments.models import Department

class Employee(models.Model):
    """
    Employee profile model.
    """

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )

    STATUS_CHOICES = (
        ("Active", "Active"),
        ("On Leave", "On Leave"),
        ("Suspended", "Suspended"),
        ("Terminated", "Terminated"),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employee_profile",
    )

    employee_number = models.CharField(
        max_length=20,
        unique=True,
    )

    phone_number = models.CharField(
        max_length=20,
    )

    national_id = models.CharField(
        max_length=20,
        unique=True,
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
    )

    date_of_birth = models.DateField()

    address = models.TextField()

    job_title = models.CharField(
        max_length=100,
    )
    
    department = models.ForeignKey(
    Department,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="employees",
)
    hire_date = models.DateField()

    profile_photo = models.ImageField(
        upload_to="employee_photos/",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active",
    )

    emergency_contact_name = models.CharField(
        max_length=100,
        blank=True,
    )

    emergency_contact_phone = models.CharField(
        max_length=20,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["employee_number"]
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.employee_number} - {self.user.get_full_name() or self.user.username}"