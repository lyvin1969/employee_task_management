from django.urls import path

from . import views

app_name = "reports"

urlpatterns = [

    path("", views.report_home, name="report_home"),

    path("dashboard/", views.dashboard_report, name="dashboard_report"),

    path("employees/", views.employee_report, name="employee_report"),

    path("departments/", views.department_report, name="department_report"),

    path("tasks/", views.task_report, name="task_report"),

    path("monthly/", views.monthly_report, name="monthly_report"),

    path("performance/", views.performance_report, name="performance_report"),

    # Export Reports
    path("export/pdf/", views.export_pdf, name="export_pdf"),

    path("export/excel/", views.export_excel, name="export_excel"),

    path("print/", views.print_report, name="print_report"),

]