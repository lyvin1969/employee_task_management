from django.urls import path

from . import views

app_name = "employees"

urlpatterns = [

    # ==========================
    # Employee List
    # ==========================
    path(
        "",
        views.employee_list,
        name="employee_list",
    ),

    # ==========================
    # Create Employee
    # ==========================
    path(
        "create/",
        views.create_employee,
        name="create_employee",
    ),

    # ==========================
    # Employee Details
    # ==========================
    path(
        "<int:pk>/",
        views.employee_detail,
        name="employee_detail",
    ),

    # ==========================
    # Update Employee
    # ==========================
    path(
        "<int:pk>/update/",
        views.update_employee,
        name="update_employee",
    ),

    # ==========================
    # Delete Employee
    # ==========================
    path(
        "<int:pk>/delete/",
        views.delete_employee,
        name="delete_employee",
    ),

    # ==========================
    # Active Employees
    # ==========================
    path(
        "active/",
        views.active_employees,
        name="active_employees",
    ),

    # ==========================
    # Search Employees
    # ==========================
    path(
        "search/",
        views.search_employee,
        name="search_employee",
    ),
]