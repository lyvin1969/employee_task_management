from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.core.exceptions import PermissionDenied

from employees.models import Employee
from departments.models import Department
from tasks.models import Task

from .forms import (
    LoginForm,
    RegisterForm,
    UserUpdateForm,
    UserProfileForm,
    CustomPasswordChangeForm,
)
from .models import CustomUser
from .permissions import (
    admin_required,
    profile_owner_or_admin,
)
from .services import UserService


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard:dashboard")

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Login successful.")
            return redirect("dashboard:dashboard")

        messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html", {"form": form})


@login_required
def logout_view(request):
    """
    Log out the current user.
    """
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("accounts:login")


@admin_required
def register(request):
    """
    Only administrators should be able to register/provision new accounts
    in a professional system.
    """
    form = RegisterForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            UserService.create_user(form)
            messages.success(request, "User created successfully.")
            return redirect("accounts:user_list")

    return render(request, "accounts/register.html", {"form": form})


@admin_required
def user_list(request):
    """
    Display all users for management. Secures access via @admin_required.
    """
    users = UserService.get_all_users()
    return render(request, "accounts/user_list.html", {"users": users})


@admin_required
def update_user(request, pk):
    """
    Update an existing user.
    """
    user = get_object_or_404(CustomUser, pk=pk)

    form = UserUpdateForm(
        request.POST or None,
        request.FILES or None,
        instance=user,
    )

    if request.method == "POST":
        if form.is_valid():
            UserService.update_user(form)
            messages.success(request, "User updated successfully.")
            return redirect("accounts:user_list")

    return render(request, "accounts/user_form.html", {
        "form": form,
        "user": user,
    })


@admin_required
def delete_user(request, pk):
    """
    Delete a user.
    """
    user = get_object_or_404(CustomUser, pk=pk)

    if request.method == "POST":
        UserService.delete_user(user)
        messages.success(request, "User deleted successfully.")
        return redirect("accounts:user_list")

    return render(request, "accounts/user_confirm_delete.html", {"user": user})


@login_required
def profile(request):
    """
    Display the logged-in user's profile.
    """
    return render(request, "accounts/profile.html", {"user": request.user})


@profile_owner_or_admin
def update_profile(request, pk):
    """
    Update a user's profile.
    """
    user = get_object_or_404(CustomUser, pk=pk)

    form = UserProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=user,
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("accounts:profile")

    return render(request, "accounts/profile.html", {
        "form": form,
        "profile_user": user,
    })


@login_required
def change_password(request):
    """
    Allow the logged-in user to change their password safely.
    """
    form = CustomPasswordChangeForm(
        request.user,
        request.POST or None,
    )

    if request.method == "POST":
        if form.is_valid():
            user = UserService.change_password(form)
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully.")
            return redirect("accounts:profile")

    return render(request, "accounts/change_password.html", {"form": form})


@login_required
def dashboard(request):
    """
    Display the core administrative/operational system dashboard.
    """
    overdue_tasks = Task.objects.filter(
        due_date__lt=timezone.now().date()
    ).exclude(status=Task.Status.COMPLETED)

    context = {
        "employee_count": Employee.objects.count(),
        "department_count": Department.objects.count(),
        "task_count": Task.objects.count(),
        "pending_tasks": Task.objects.filter(status=Task.Status.PENDING).count(),
        "in_progress_tasks": Task.objects.filter(status=Task.Status.IN_PROGRESS).count(),
        "review_tasks": Task.objects.filter(status=Task.Status.REVIEW).count(),
        "completed_tasks": Task.objects.filter(status=Task.Status.COMPLETED).count(),
        "cancelled_tasks": Task.objects.filter(status=Task.Status.CANCELLED).count(),
        "overdue_tasks": overdue_tasks.count(),
        "recent_tasks": Task.objects.order_by("-created_at")[:5],
        "recent_employees": Employee.objects.order_by("-created_at")[:5],
    }

    return render(request, "dashboard/dashboard.html", context)