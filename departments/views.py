from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from notifications.models import Notification
from notifications.services import NotificationService

from .forms import DepartmentForm, DepartmentUpdateForm
from .models import Department
from .services import DepartmentService


@login_required
def department_list(request):
    """
    Display all departments.
    """

    departments = DepartmentService.get_all_departments()

    return render(
        request,
        "departments/department_list.html",
        {
            "departments": departments,
        },
    )


@login_required
def create_department(request):
    """
    Create a new department.
    """

    form = DepartmentForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():

            department = DepartmentService.create_department(form)

            NotificationService.create_notification(
                recipient=request.user,
                title="Department Created",
                message=f"{department.department_name} department has been created successfully.",
                notification_type=Notification.NotificationType.DEPARTMENT,
            )

            messages.success(
                request,
                "Department created successfully."
            )

            return redirect("departments:department_list")

    return render(
        request,
        "departments/department_form.html",
        {
            "form": form,
        },
    )


@login_required
def department_detail(request, pk):
    """
    Display one department.
    """

    department = get_object_or_404(
        Department,
        pk=pk,
    )

    return render(
        request,
        "departments/department_detail.html",
        {
            "department": department,
        },
    )


@login_required
def update_department(request, pk):
    """
    Update an existing department.
    """

    department = get_object_or_404(
        Department,
        pk=pk,
    )

    form = DepartmentUpdateForm(
        request.POST or None,
        instance=department,
    )

    if request.method == "POST":

        if form.is_valid():

            department = DepartmentService.update_department(form)

            NotificationService.create_notification(
                recipient=request.user,
                title="Department Updated",
                message=f"{department.department_name} department has been updated.",
                notification_type=Notification.NotificationType.DEPARTMENT,
            )

            messages.success(
                request,
                "Department updated successfully."
            )

            return redirect(
                "departments:department_detail",
                pk=department.pk,
            )

    return render(
        request,
        "departments/department_form.html",
        {
            "form": form,
            "department": department,
        },
    )


@login_required
def delete_department(request, pk):
    """
    Delete a department.
    """

    department = get_object_or_404(
        Department,
        pk=pk,
    )

    if request.method == "POST":

        department_name = department.department_name

        DepartmentService.delete_department(department)

        NotificationService.create_notification(
            recipient=request.user,
            title="Department Deleted",
            message=f"{department_name} department has been deleted.",
            notification_type=Notification.NotificationType.DEPARTMENT,
        )

        messages.success(
            request,
            "Department deleted successfully."
        )

        return redirect(
            "departments:department_list"
        )

    return render(
        request,
        "departments/department_delete.html",
        {
            "department": department,
        },
    )


@login_required
def active_departments(request):
    """
    Display active departments.
    """

    departments = DepartmentService.get_active_departments()

    return render(
        request,
        "departments/department_list.html",
        {
            "departments": departments,
        },
    )


@login_required
def search_department(request):
    """
    Search departments.
    """

    query = request.GET.get("q", "").strip()

    departments = DepartmentService.search_departments(query)

    return render(
        request,
        "departments/department_list.html",
        {
            "departments": departments,
            "query": query,
        },
    )