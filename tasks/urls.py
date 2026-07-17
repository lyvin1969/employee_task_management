from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [

    # ==========================
    # Task List
    # ==========================
    path(
        "",
        views.task_list,
        name="task_list",
    ),

    # ==========================
    # Create Task
    # ==========================
    path(
        "create/",
        views.create_task,
        name="create_task",
    ),

    # ==========================
    # Task Detail
    # ==========================
    path(
        "<int:pk>/",
        views.task_detail,
        name="task_detail",
    ),

    # ==========================
    # Update Task
    # ==========================
    path(
        "<int:pk>/update/",
        views.update_task,
        name="update_task",
    ),

    # ==========================
    # Delete Task
    # ==========================
    path(
        "<int:pk>/delete/",
        views.delete_task,
        name="delete_task",
    ),

    # ==========================
    # Search Tasks
    # ==========================
    path(
        "search/",
        views.search_task,
        name="search_task",
    ),

    # ==========================
    # Pending Tasks
    # ==========================
    path(
        "pending/",
        views.pending_tasks,
        name="pending_tasks",
    ),

    # ==========================
    # In Progress Tasks
    # ==========================
    path(
        "in-progress/",
        views.in_progress_tasks,
        name="in_progress_tasks",
    ),

    # ==========================
    # Completed Tasks
    # ==========================
    path(
        "completed/",
        views.completed_tasks,
        name="completed_tasks",
    ),

    # ==========================
    # Overdue Tasks
    # ==========================
    path(
        "overdue/",
        views.overdue_tasks,
        name="overdue_tasks",
    ),

    # ==========================
    # High Priority Tasks
    # ==========================
    path(
        "high-priority/",
        views.high_priority_tasks,
        name="high_priority_tasks",
    ),
]