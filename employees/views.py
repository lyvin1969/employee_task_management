from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EmployeeForm, EmployeeUpdateForm
from .models import Employee
from .services import EmployeeService

from notifications.models import Notification
from notifications.services import NotificationService


@login_required
def employee_list(request):
    """
    Display all employees.
    """

    employees = EmployeeService.get_all_employees()

    return render(
        request,
        "employees/employee_list.html",
        {
            "employees": employees,
        },
    )


@login_required
def employee_detail(request, pk):
    """
    Display employee details.
    """

    employee = get_object_or_404(Employee, pk=pk)

    return render(
        request,
        "employees/employee_detail.html",
        {
            "employee": employee,
        },
    )


@login_required
def create_employee(request):
    """
    Create a new employee.
    """

    form = EmployeeForm(request.POST or None, request.FILES or None)

    if request.method == "POST":

        if form.is_valid():

            employee = EmployeeService.create_employee(form)

            NotificationService.create_notification(
                recipient=request.user,
                title="New Employee Added",
                message=f"{employee.user.get_full_name() or employee.user.username} has been added successfully.",
                notification_type=Notification.NotificationType.EMPLOYEE,
            )

            messages.success(
                request,
                "Employee created successfully."
            )

            return redirect("employees:employee_list")

    return render(
        request,
        "employees/employee_form.html",
        {
            "form": form,
        },
    )


@login_required
def update_employee(request, pk):
    """
    Update employee information.
    """

    employee = get_object_or_404(Employee, pk=pk)

    form = EmployeeUpdateForm(
        request.POST or None,
        request.FILES or None,
        instance=employee,
    )

    if request.method == "POST":

        if form.is_valid():

            employee = EmployeeService.update_employee(form)

            NotificationService.create_notification(
                recipient=request.user,
                title="Employee Updated",
                message=f"{employee.user.get_full_name() or employee.user.username}'s details were updated.",
                notification_type=Notification.NotificationType.EMPLOYEE,
            )

            messages.success(
                request,
                "Employee updated successfully."
            )

            return redirect(
                "employees:employee_detail",
                pk=employee.pk,
            )

    return render(
        request,
        "employees/employee_update.html",
        {
            "form": form,
            "employee": employee,
        },
    )


@login_required
def delete_employee(request, pk):
    """
    Delete employee.
    """

    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":

        employee_name = (
            employee.user.get_full_name()
            or employee.user.username
        )

        EmployeeService.delete_employee(employee)

        NotificationService.create_notification(
            recipient=request.user,
            title="Employee Deleted",
            message=f"{employee_name} has been removed from the system.",
            notification_type=Notification.NotificationType.EMPLOYEE,
        )

        messages.success(
            request,
            "Employee deleted successfully."
        )

        return redirect("employees:employee_list")

    return render(
        request,
        "employees/employee_delete.html",
        {
            "employee": employee,
        },
    )


@login_required
def active_employees(request):
    """
    Display active employees.
    """

    employees = EmployeeService.get_active_employees()

    return render(
        request,
        "employees/employee_list.html",
        {
            "employees": employees,
        },
    )


@login_required
def search_employee(request):
    """
    Search employees.
    """

    query = request.GET.get("q", "").strip()

    employees = []

    if query:
        employees = EmployeeService.search_employees(query)

    return render(
        request,
        "employees/employee_list.html",
        {
            "employees": employees,
            "query": query,
        },
    )