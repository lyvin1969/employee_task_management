from .models import Department


class DepartmentService:
    """
    Service class for department operations.
    """

    @staticmethod
    def get_all_departments():
        """
        Return all departments.
        """
        return Department.objects.all()

    @staticmethod
    def get_active_departments():
        """
        Return only active departments.
        """
        return Department.objects.filter(
            is_active=True
        )

    @staticmethod
    def create_department(form):
        """
        Create a new department.
        """
        return form.save()

    @staticmethod
    def update_department(form):
        """
        Update an existing department.
        """
        return form.save()

    @staticmethod
    def delete_department(department):
        """
        Delete a department.
        """
        department.delete()

    @staticmethod
    def search_departments(query):
        """
        Search departments by name or code.
        """

        return Department.objects.filter(
            department_name__icontains=query
        ) | Department.objects.filter(
            department_code__icontains=query
        )

    @staticmethod
    def get_department(pk):
        """
        Return one department by ID.
        """

        return Department.objects.get(pk=pk)

    @staticmethod
    def department_exists(name):
        """
        Check if department exists.
        """

        return Department.objects.filter(
            department_name__iexact=name
        ).exists()