from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from openpyxl import Workbook

from departments.models import Department
from employees.models import Employee
from tasks.models import Task

from notifications.models import Notification
from notifications.services import NotificationService


@login_required
def report_home(request):
    """
    Reports Dashboard
    """

    NotificationService.create_notification(
        recipient=request.user,
        title="Reports Dashboard",
        message="Reports dashboard accessed successfully.",
        notification_type=Notification.NotificationType.REPORT,
    )

    all_tasks = Task.objects.select_related(
        "assigned_to",
        "assigned_by",
    ).all()

    recent_tasks = all_tasks.order_by("-created_at")[:5]

    recent_employees = Employee.objects.select_related(
        "user"
    ).order_by("-id")[:5]

    context = {

        "employee_count": Employee.objects.count(),

        "department_count": Department.objects.count(),

        "task_count": Task.objects.count(),

        "completed_tasks": Task.objects.filter(
            status=Task.Status.COMPLETED
        ).count(),

        "pending_tasks": Task.objects.filter(
            status=Task.Status.PENDING
        ).count(),

        "in_progress_tasks": Task.objects.filter(
            status=Task.Status.IN_PROGRESS
        ).count(),

        "review_tasks": Task.objects.filter(
            status=Task.Status.REVIEW
        ).count(),

        "cancelled_tasks": Task.objects.filter(
            status=Task.Status.CANCELLED
        ).count(),

        "overdue_tasks": sum(
            1 for task in all_tasks if task.is_overdue
        ),

        "recent_tasks": recent_tasks,

        "recent_employees": recent_employees,

        "chart_data": {

            "completed": Task.objects.filter(
                status=Task.Status.COMPLETED
            ).count(),

            "pending": Task.objects.filter(
                status=Task.Status.PENDING
            ).count(),

            "progress": Task.objects.filter(
                status=Task.Status.IN_PROGRESS
            ).count(),

            "review": Task.objects.filter(
                status=Task.Status.REVIEW
            ).count(),

            "cancelled": Task.objects.filter(
                status=Task.Status.CANCELLED
            ).count(),
        },
    }

    return render(
        request,
        "reports/report_home.html",
        context,
    )


@login_required
def dashboard_report(request):
    """
    Dashboard statistics report.
    """

    context = {

        "employee_count": Employee.objects.count(),

        "department_count": Department.objects.count(),

        "task_count": Task.objects.count(),

        "completed_tasks": Task.objects.filter(
            status=Task.Status.COMPLETED
        ).count(),

        "pending_tasks": Task.objects.filter(
            status=Task.Status.PENDING
        ).count(),

    }

    return render(
        request,
        "reports/dashboard.html",
        context,
    )


@login_required
def employee_report(request):
    """
    Employee report.
    """

    employees = Employee.objects.select_related(
        "user"
    ).all()

    NotificationService.create_notification(
        recipient=request.user,
        title="Employee Report",
        message="Employee report generated successfully.",
        notification_type=Notification.NotificationType.REPORT,
    )

    return render(
        request,
        "reports/employee_report.html",
        {
            "employees": employees,
        },
    )


@login_required
def department_report(request):
    """
    Department report.
    """

    departments = Department.objects.all()

    NotificationService.create_notification(
        recipient=request.user,
        title="Department Report",
        message="Department report generated successfully.",
        notification_type=Notification.NotificationType.REPORT,
    )

    return render(
        request,
        "reports/department_report.html",
        {
            "departments": departments,
        },
    )
    
@login_required
def task_report(request):
    """
    Task report.
    """

    tasks = Task.objects.select_related(
        "assigned_to",
        "assigned_by",
    ).all()

    NotificationService.create_notification(
        recipient=request.user,
        title="Task Report",
        message="Task report generated successfully.",
        notification_type=Notification.NotificationType.REPORT,
    )

    return render(
        request,
        "reports/task_report.html",
        {
            "tasks": tasks,
        },
    )


@login_required
def monthly_report(request):
    """
    Monthly report.
    """

    NotificationService.create_notification(
        recipient=request.user,
        title="Monthly Report",
        message="Monthly report generated successfully.",
        notification_type=Notification.NotificationType.REPORT,
    )

    return render(
        request,
        "reports/monthly_report.html",
    )


@login_required
def performance_report(request):
    """
    Employee performance report.
    """

    employees = Employee.objects.select_related(
        "user",
    ).all()

    NotificationService.create_notification(
        recipient=request.user,
        title="Performance Report",
        message="Performance report generated successfully.",
        notification_type=Notification.NotificationType.REPORT,
    )

    return render(
        request,
        "reports/performance_report.html",
        {
            "employees": employees,
        },
    )


@login_required
def export_pdf(request):
    """
    Export system report to PDF.
    """

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = (
        'attachment; filename="Employee_Task_Report.pdf"'
    )

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Employee Task Management System",
            styles["Title"],
        )
    )

    elements.append(
        Paragraph(
            "System Summary Report",
            styles["Heading2"],
        )
    )

    elements.append(Spacer(1, 20))

    data = [

        ["Category", "Total"],

        ["Employees", Employee.objects.count()],

        ["Departments", Department.objects.count()],

        ["Tasks", Task.objects.count()],

        [
            "Completed Tasks",
            Task.objects.filter(
                status=Task.Status.COMPLETED
            ).count(),
        ],

        [
            "Pending Tasks",
            Task.objects.filter(
                status=Task.Status.PENDING
            ).count(),
        ],

        [
            "In Progress",
            Task.objects.filter(
                status=Task.Status.IN_PROGRESS
            ).count(),
        ],

        [
            "Under Review",
            Task.objects.filter(
                status=Task.Status.REVIEW
            ).count(),
        ],

        [
            "Cancelled",
            Task.objects.filter(
                status=Task.Status.CANCELLED
            ).count(),
        ],

    ]

    table = Table(data)

    table.setStyle(TableStyle([

        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),

        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

        ("GRID", (0, 0), (-1, -1), 1, colors.black),

    ]))

    elements.append(table)

    doc.build(elements)

    NotificationService.create_notification(
        recipient=request.user,
        title="PDF Export",
        message="System report exported as PDF successfully.",
        notification_type=Notification.NotificationType.REPORT,
    )

    return response


@login_required
def export_excel(request):
    """
    Export system report to Excel.
    """

    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "System Report"

    sheet.append(["Category", "Total"])

    sheet.append(["Employees", Employee.objects.count()])

    sheet.append(["Departments", Department.objects.count()])

    sheet.append(["Tasks", Task.objects.count()])

    sheet.append([
        "Completed Tasks",
        Task.objects.filter(
            status=Task.Status.COMPLETED
        ).count()
    ])

    sheet.append([
        "Pending Tasks",
        Task.objects.filter(
            status=Task.Status.PENDING
        ).count()
    ])

    sheet.append([
        "In Progress",
        Task.objects.filter(
            status=Task.Status.IN_PROGRESS
        ).count()
    ])

    sheet.append([
        "Under Review",
        Task.objects.filter(
            status=Task.Status.REVIEW
        ).count()
    ])

    sheet.append([
        "Cancelled",
        Task.objects.filter(
            status=Task.Status.CANCELLED
        ).count()
    ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="Employee_Task_Report.xlsx"'
    )

    workbook.save(response)

    NotificationService.create_notification(
        recipient=request.user,
        title="Excel Export",
        message="System report exported as Excel successfully.",
        notification_type=Notification.NotificationType.REPORT,
    )

    return response


@login_required
def print_report(request):
    """
    Printable report.
    """

    context = {

        "employee_count": Employee.objects.count(),

        "department_count": Department.objects.count(),

        "task_count": Task.objects.count(),

        "completed_tasks": Task.objects.filter(
            status=Task.Status.COMPLETED
        ).count(),

        "pending_tasks": Task.objects.filter(
            status=Task.Status.PENDING
        ).count(),

        "in_progress_tasks": Task.objects.filter(
            status=Task.Status.IN_PROGRESS
        ).count(),

        "review_tasks": Task.objects.filter(
            status=Task.Status.REVIEW
        ).count(),

        "cancelled_tasks": Task.objects.filter(
            status=Task.Status.CANCELLED
        ).count(),

    }

    NotificationService.create_notification(
        recipient=request.user,
        title="Print Report",
        message="Print report opened successfully.",
        notification_type=Notification.NotificationType.REPORT,
    )

    return render(
        request,
        "reports/print_report.html",
        context,
    )