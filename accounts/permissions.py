from functools import wraps

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def admin_required(view_func):
    """
    Allows access to administrators only. Includes superuser protection.
    """

    @login_required
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Always allow superusers or explicit admin roles (case-insensitive checking)
        user_role = str(getattr(request.user, "role", "")).upper()
        admin_constant = str(getattr(request.user, "ADMIN", "ADMIN")).upper()

        if request.user.is_superuser or user_role == admin_constant or user_role == "ADMIN":
            return view_func(request, *args, **kwargs)

        messages.error(request, "You do not have permission to access this page.")
        return redirect("dashboard:dashboard")

    return wrapper


def manager_required(view_func):
    """
    Allows access to managers only.
    """

    @login_required
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user_role = str(getattr(request.user, "role", "")).upper()
        manager_constant = str(getattr(request.user, "MANAGER", "MANAGER")).upper()

        if request.user.is_superuser or user_role == manager_constant or user_role == "MANAGER":
            return view_func(request, *args, **kwargs)

        messages.error(request, "You do not have permission to access this page.")
        return redirect("dashboard:dashboard")

    return wrapper


def employee_required(view_func):
    """
    Allows access to employees only.
    """

    @login_required
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user_role = str(getattr(request.user, "role", "")).upper()
        employee_constant = str(getattr(request.user, "EMPLOYEE", "EMPLOYEE")).upper()

        if user_role == employee_constant or user_role == "EMPLOYEE":
            return view_func(request, *args, **kwargs)

        messages.error(request, "You do not have permission to access this page.")
        return redirect("dashboard:dashboard")

    return wrapper


def admin_or_manager_required(view_func):
    """
    Allows access to administrators and managers.
    """

    @login_required
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user_role = str(getattr(request.user, "role", "")).upper()
        admin_constant = str(getattr(request.user, "ADMIN", "ADMIN")).upper()
        manager_constant = str(getattr(request.user, "MANAGER", "MANAGER")).upper()

        if (
            request.user.is_superuser
            or user_role in [admin_constant, manager_constant, "ADMIN", "MANAGER"]
        ):
            return view_func(request, *args, **kwargs)

        messages.error(request, "You do not have permission to access this page.")
        return redirect("dashboard:dashboard")

    return wrapper


def profile_owner_or_admin(view_func):
    """
    Allows users to edit their own profile or administrators to edit any profile.
    """

    @login_required
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user_id = kwargs.get("pk")
        user_role = str(getattr(request.user, "role", "")).upper()
        admin_constant = str(getattr(request.user, "ADMIN", "ADMIN")).upper()

        if (
            request.user.is_superuser
            or user_role == admin_constant
            or user_role == "ADMIN"
            or request.user.id == user_id
        ):
            return view_func(request, *args, **kwargs)

        messages.error(request, "You do not have permission to perform this action.")
        return redirect("dashboard:dashboard")

    return wrapper