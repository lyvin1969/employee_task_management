from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm,
)

User = get_user_model()


class LoginForm(AuthenticationForm):
    """
    Custom Login Form
    """

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your username",
                "autofocus": True,
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password",
            }
        )
    )


class RegisterForm(UserCreationForm):
    """
    Form for registering new users.
    """

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "phone",
            "role",
            "profile_picture",
            "password1",
            "password2",
        )

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "First Name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Last Name",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Username",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Address",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone Number",
                }
            ),
            "role": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "profile_picture": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm Password",
            }
        )
    )


class UserUpdateForm(forms.ModelForm):
    """
    Form for administrators to update user details.
    """

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "phone",
            "role",
            "profile_picture",
            "is_active",
        )

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "username": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "role": forms.Select(
                attrs={"class": "form-select"}
            ),
            "profile_picture": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
        }


class UserProfileForm(forms.ModelForm):
    """
    Form for users to update their own profile.
    """

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone",
            "profile_picture",
        )

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "profile_picture": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    """
    Custom Password Change Form
    """

    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Current Password",
            }
        )
    )

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "New Password",
            }
        )
    )

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm New Password",
            }
        )
    )