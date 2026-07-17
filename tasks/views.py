from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm, TaskUpdateForm
from .models import Task
from .services import TaskService

from notifications.services import NotificationService
from notifications.models import Notification

def task_statistics():
    """
    Returns task summary statistics for the dashboard cards.
    """
    return {
        "pending_count": Task.objects.filter(
            status=Task.Status.PENDING
        ).count(),

        "completed_count": Task.objects.filter(
            status=Task.Status.COMPLETED
        ).count(),

        "overdue_count": TaskService.overdue_tasks().count(),

        "total_tasks": Task.objects.count(),
    }


@login_required
def task_list(request):
    """
    Display all tasks.
    """
    tasks = TaskService.get_all_tasks()

    context = {
        "tasks": tasks,
        **task_statistics(),
    }

    return render(
        request,
        "tasks/task_list.html",
        context,
    )


@login_required
def create_task(request):
    """
    Create a new task.
    """
    form = TaskForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            TaskService.create_task(form, request.user)
            NotificationService.create_notification(
    recipient=request.user,
    title="New Task Created",
    message="A new task has been created successfully.",
    notification_type=Notification.NotificationType.TASK,
)

            messages.success(
                request,
                "Task created successfully."
            )

            return redirect("tasks:task_list")

    return render(
        request,
        "tasks/task_form.html",
        {
            "form": form,
        },
    )


@login_required
def task_detail(request, pk):
    """
    Display task details.
    """
    task = get_object_or_404(Task, pk=pk)

    return render(
        request,
        "tasks/task_detail.html",
        {
            "task": task,
        },
    )


@login_required
def update_task(request, pk):
    """
    Update a task.
    """
    task = get_object_or_404(Task, pk=pk)

    form = TaskUpdateForm(
        request.POST or None,
        instance=task,
    )

    if request.method == "POST":
        if form.is_valid():
            TaskService.update_task(form)

            messages.success(
                request,
                "Task updated successfully."
            )

            return redirect(
                "tasks:task_detail",
                pk=task.pk,
            )

    return render(
        request,
        "tasks/task_form.html",
        {
            "form": form,
            "task": task,
        },
    )


@login_required
def delete_task(request, pk):
    """
    Delete a task.
    """
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        TaskService.delete_task(task)

        messages.success(
            request,
            "Task deleted successfully."
        )

        return redirect("tasks:task_list")

    return render(
        request,
        "tasks/task_delete.html",
        {
            "task": task,
        },
    )


@login_required
def search_task(request):
    """
    Search tasks.
    """
    query = request.GET.get("q", "")

    tasks = TaskService.search_tasks(query)

    context = {
        "tasks": tasks,
        "query": query,
        **task_statistics(),
    }

    return render(
        request,
        "tasks/task_list.html",
        context,
    )


@login_required
def pending_tasks(request):
    """
    Display pending tasks.
    """
    tasks = TaskService.pending_tasks()

    context = {
        "tasks": tasks,
        **task_statistics(),
    }

    return render(
        request,
        "tasks/task_list.html",
        context,
    )


@login_required
def in_progress_tasks(request):
    """
    Display tasks currently in progress.
    """
    tasks = TaskService.in_progress_tasks()

    context = {
        "tasks": tasks,
        **task_statistics(),
    }

    return render(
        request,
        "tasks/task_list.html",
        context,
    )


@login_required
def completed_tasks(request):
    """
    Display completed tasks.
    """
    tasks = TaskService.completed_tasks()

    context = {
        "tasks": tasks,
        **task_statistics(),
    }

    return render(
        request,
        "tasks/task_list.html",
        context,
    )


@login_required
def overdue_tasks(request):
    """
    Display overdue tasks.
    """
    tasks = TaskService.overdue_tasks()

    context = {
        "tasks": tasks,
        **task_statistics(),
    }

    return render(
        request,
        "tasks/task_list.html",
        context,
    )


@login_required
def high_priority_tasks(request):
    """
    Display high-priority tasks.
    """
    tasks = TaskService.high_priority_tasks()

    context = {
        "tasks": tasks,
        **task_statistics(),
    }

    return render(
        request,
        "tasks/task_list.html",
        context,
    )