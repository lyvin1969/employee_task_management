from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from employees.models import Employee
from departments.models import Department
from tasks.models import Task
from tasks.services import TaskService


@login_required
def dashboard(request):

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

        "overdue_tasks": TaskService.overdue_tasks().count(),

        "recent_tasks": Task.objects.order_by("-created_at")[:5],

        "recent_employees": Employee.objects.order_by("-created_at")[:5],

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )