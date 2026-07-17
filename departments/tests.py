from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Department

User = get_user_model()


class DepartmentTests(TestCase):
    """
    Test cases for the Departments app.
    """

    def setUp(self):
        """
        Create a test user and department.
        """

        self.user = User.objects.create_user(
            username="admin",
            password="admin123",
            first_name="System",
            last_name="Administrator",
            email="admin@example.com",
        )

        self.client.login(
            username="admin",
            password="admin123",
        )

        self.department = Department.objects.create(
            department_name="Information Technology",
            department_code="IT001",
            manager=self.user,
            email="it@example.com",
            phone_number="0712345678",
            location="Main Office",
            description="Handles all IT operations.",
            is_active=True,
        )

    def test_department_list_page(self):
        """
        Department list page loads successfully.
        """

        response = self.client.get(
            reverse("departments:department_list")
        )

        self.assertEqual(response.status_code, 200)

    def test_create_department(self):
        """
        Create a department.
        """

        response = self.client.post(
            reverse("departments:create_department"),
            {
                "department_name": "Finance",
                "department_code": "FIN001",
                "manager": self.user.id,
                "email": "finance@example.com",
                "phone_number": "0700111222",
                "location": "Block B",
                "description": "Finance Department",
                "is_active": True,
            },
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Department.objects.filter(
                department_name="Finance"
            ).exists()
        )

    def test_update_department(self):
        """
        Update an existing department.
        """

        response = self.client.post(
            reverse(
                "departments:update_department",
                args=[self.department.pk],
            ),
            {
                "department_name": "ICT",
                "department_code": "ICT001",
                "manager": self.user.id,
                "email": "ict@example.com",
                "phone_number": "0711000000",
                "location": "Block C",
                "description": "ICT Department",
                "is_active": True,
            },
        )

        self.assertEqual(response.status_code, 302)

        self.department.refresh_from_db()

        self.assertEqual(
            self.department.department_name,
            "ICT",
        )

    def test_delete_department(self):
        """
        Delete a department.
        """

        response = self.client.post(
            reverse(
                "departments:delete_department",
                args=[self.department.pk],
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertFalse(
            Department.objects.filter(
                pk=self.department.pk
            ).exists()
        )

    def test_search_department(self):
        """
        Search departments.
        """

        response = self.client.get(
            reverse("departments:search_department"),
            {
                "q": "Information",
            },
        )

        self.assertEqual(response.status_code, 200)

    def test_active_departments(self):
        """
        Active departments page.
        """

        response = self.client.get(
            reverse(
                "departments:active_departments"
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_department_string(self):
        """
        Test __str__ method.
        """

        self.assertEqual(
            str(self.department),
            "Information Technology (IT001)",
        )