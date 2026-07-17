from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()


class UserService:
    """
    Service class for handling user-related business logic.
    """

    @staticmethod
    def create_user(form):
        """
        Create a new user from a validated form.
        """
        return form.save()

    @staticmethod
    def update_user(form):
        """
        Update an existing user from a validated form.
        """
        return form.save()

    @staticmethod
    def delete_user(user):
        """
        Delete a user.
        """
        user.delete()

    @staticmethod
    def get_user_by_id(user_id):
        """
        Retrieve a user by their ID.
        """
        return User.objects.filter(pk=user_id).first()

    @staticmethod
    def get_all_users():
        """
        Retrieve all users ordered by first name.
        """
        return User.objects.all().order_by("first_name", "last_name")

    @staticmethod
    def authenticate_user(username, password):
        """
        Authenticate a user.
        """
        return authenticate(
            username=username,
            password=password
        )

    @staticmethod
    def change_password(form):
        """
        Save a new password using PasswordChangeForm.
        """
        return form.save()

    @staticmethod
    def activate_user(user):
        """
        Activate a user account.
        """
        user.is_active = True
        user.save(update_fields=["is_active"])

    @staticmethod
    def deactivate_user(user):
        """
        Deactivate a user account.
        """
        user.is_active = False
        user.save(update_fields=["is_active"])

    @staticmethod
    def get_users_by_role(role):
        """
        Retrieve users with a specific role.
        """
        return User.objects.filter(role=role)

    @staticmethod
    def get_active_users():
        """
        Retrieve all active users.
        """
        return User.objects.filter(is_active=True)

    @staticmethod
    def get_inactive_users():
        """
        Retrieve all inactive users.
        """
        return User.objects.filter(is_active=False)