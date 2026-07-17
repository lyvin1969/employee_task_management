from django.urls import path

from . import views

app_name = "departments"

urlpatterns = [

    # ==========================
    # Department List
    # ==========================
    path(
        "",
        views.department_list,
        name="department_list",
    ),

    # ==========================
    # Create Department
    # ==========================
    path(
        "create/",
        views.create_department,
        name="create_department",
    ),

    # ==========================
    # Department Details
    # ==========================
    path(
        "<int:pk>/",
        views.department_detail,
        name="department_detail",
    ),

    # ==========================
    # Update Department
    # ==========================
    path(
        "<int:pk>/update/",
        views.update_department,
        name="update_department",
    ),

    # ==========================
    # Delete Department
    # ==========================
    path(
        "<int:pk>/delete/",
        views.delete_department,
        name="delete_department",
    ),

    # ==========================
    # Active Departments
    # ==========================
    path(
        "active/",
        views.active_departments,
        name="active_departments",
    ),

    # ==========================
    # Search Departments
    # ==========================
    path(
        "search/",
        views.search_department,
        name="search_department",
    ),
]