from django.db.models import Q
from .models import Task


class TaskService:
    """
    Handles business logic for Task operations.
    """

    @staticmethod
    def get_all_tasks():
        """
        Return all tasks ordered by newest first.
        """
        return Task.objects.select_related(
            "assigned_to",
            "assigned_by",
        ).all()

    @staticmethod
    def get_task(pk):
        """
        Return a single task.
        """
        return Task.objects.select_related(
            "assigned_to",
            "assigned_by",
        ).get(pk=pk)

    @staticmethod
    def create_task(form, assigned_by):
        """
        Create a new task.
        """
        task = form.save(commit=False)
        task.assigned_by = assigned_by
        task.save()
        return task

    @staticmethod
    def update_task(form):
        """
        Update an existing task.
        """
        return form.save()

    @staticmethod
    def delete_task(task):
        """
        Delete a task.
        """
        task.delete()

    @staticmethod
    def search_tasks(query):
        """
        Search tasks.
        """
        if not query:
            return Task.objects.select_related("assigned_to", "assigned_by").all()

        return Task.objects.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(assigned_to__user__first_name__icontains=query)
            | Q(assigned_to__user__last_name__icontains=query)
            | Q(assigned_to__user__username__icontains=query)
            | Q(priority__icontains=query)
            | Q(status__icontains=query)
        ).select_related(
            "assigned_to",
            "assigned_by",
        ).distinct()

    @staticmethod
    def pending_tasks():
        """
        Return pending tasks.
        """
        return Task.objects.filter(
            status=Task.Status.PENDING
        )

    @staticmethod
    def in_progress_tasks():
        """
        Return tasks currently in progress.
        """
        return Task.objects.filter(
            status=Task.Status.IN_PROGRESS
        )

    @staticmethod
    def completed_tasks():
        """
        Return completed tasks.
        """
        return Task.objects.filter(
            status=Task.Status.COMPLETED
        )

    @staticmethod
    def overdue_tasks():
        """
        Return overdue tasks.
        """
        from django.utils import timezone

        return Task.objects.filter(
            due_date__lt=timezone.now().date()
        ).exclude(
            status=Task.Status.COMPLETED
        )

    @staticmethod
    def high_priority_tasks():
        """
        Return high and critical priority tasks.
        """
        return Task.objects.filter(
            priority__in=[
                Task.Priority.HIGH,
                Task.Priority.CRITICAL,
            ]
        )