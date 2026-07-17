from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountTests(TestCase):
    """
    Test cases for the Accounts app.
    """

    def setUp(self):
        """
        Create a test user.
        """

        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="Test@12345",
            first_name="Test",
            last_name="User",
        )

    def test_user_creation(self):
        """
        Test that a user is created successfully.
        """

        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.check_password("Test@12345"))

    def test_login(self):
        """
        Test user login.
        """

        response = self.client.login(
            username="testuser",
            password="Test@12345"
        )

        self.assertTrue(response)

    def test_profile_requires_login(self):
        """
        Profile page should require authentication.
        """

        response = self.client.get(
            reverse("accounts:profile")
        )

        self.assertEqual(response.status_code, 302)

    def test_login_page_loads(self):
        """
        Login page loads successfully.
        """

        response = self.client.get(
            reverse("accounts:login")
        )

        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """
        Test logout functionality.
        """

        self.client.login(
            username="testuser",
            password="Test@12345"
        )

        response = self.client.get(
            reverse("accounts:logout")
        )

        self.assertEqual(response.status_code, 302)