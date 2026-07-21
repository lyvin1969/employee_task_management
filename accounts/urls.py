from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    # ==========================
    # Temporary Setup Route
    # ==========================
    path(
        "make-me-admin/",
        views.create_admin_view,
        name="make_me_admin",
    ),
    # ==========================
    # Authentication
    # ==========================
    path(
        "login/",
        views.login_view,
        name="login",
    ),
    path(
        "logout/",
        views.logout_view,
        name="logout",
    ),
    path(
        "register/",
        views.register,
        name="register",
    ),
    # ==========================
    # Profile
    # ==========================
    path(
        "profile/",
        views.profile,
        name="profile",
    ),
    path(
        "profile/<int:pk>/edit/",
        views.update_profile,
        name="update_profile",
    ),
    path(
        "change-password/",
        views.change_password,
        name="change_password",
    ),
    # ==========================
    # User Management
    # ==========================
    path(
        "users/",
        views.user_list,
        name="user_list",
    ),
    path(
        "users/<int:pk>/edit/",
        views.update_user,
        name="update_user",
    ),
    path(
        "users/<int:pk>/delete/",
        views.delete_user,
        name="delete_user",
    ),
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard",
    ),
]