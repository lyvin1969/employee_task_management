from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Employee

User = get_user_model()


class EmployeeTests(TestCase):
    """
    Employee app tests.
    """

    def setUp(self):
        """
        Create a test user and employee.
        """

        self.user = User.objects.create_user(
            username="admin",
            email="admin@example.com",
            password="admin123",
            first_name="System",
            last_name="Administrator",
        )

        self.client.login(
            username="admin",
            password="admin123"
        )

        self.employee = Employee.objects.create(
            user=self.user,
            employee_number="EMP001",
            phone_number="0712345678",
            national_id="12345678",
            gender="Male",
            date_of_birth="1998-05-20",
            address="Nairobi, Kenya",
            job_title="Software Developer",
            hire_date="2026-01-01",
            status="Active",
            emergency_contact_name="John Doe",
            emergency_contact_phone="0700111222",
        )

    def test_employee_created(self):
        """
        Employee is created successfully.
        """

        self.assertEqual(
            self.employee.employee_number,
            "EMP001"
        )

        self.assertEqual(
            self.employee.job_title,
            "Software Developer"
        )

    def test_employee_list_page(self):
        """
        Employee list page loads.
        """

        response = self.client.get(
            reverse("employees:employee_list")
        )

        self.assertEqual(response.status_code, 200)

    def test_employee_detail_page(self):
        """
        Employee detail page loads.
        """

        response = self.client.get(
            reverse(
                "employees:employee_detail",
                args=[self.employee.pk]
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_create_employee_page(self):
        """
        Employee creation page loads.
        """

        response = self.client.get(
            reverse("employees:create_employee")
        )

        self.assertEqual(response.status_code, 200)

    def test_update_employee_page(self):
        """
        Employee update page loads.
        """

        response = self.client.get(
            reverse(
                "employees:update_employee",
                args=[self.employee.pk]
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_delete_employee_page(self):
        """
        Employee delete confirmation page loads.
        """

        response = self.client.get(
            reverse(
                "employees:delete_employee",
                args=[self.employee.pk]
            )
        )

        self.assertEqual(response.status_code, 200)