from .models import Employee


class EmployeeService:
    """
    Business logic for Employee operations.
    """

    @staticmethod
    def create_employee(form):
        """
        Create a new employee.
        """
        return form.save()

    @staticmethod
    def update_employee(form):
        """
        Update an existing employee.
        """
        return form.save()

    @staticmethod
    def delete_employee(employee):
        """
        Delete an employee.
        """
        employee.delete()

    @staticmethod
    def get_all_employees():
        """
        Return all employees.
        """
        return Employee.objects.select_related("user").all()

    @staticmethod
    def get_employee_by_id(pk):
        """
        Return a single employee by ID.
        """
        return Employee.objects.select_related("user").get(pk=pk)

    @staticmethod
    def get_active_employees():
        """
        Return all active employees.
        """
        return Employee.objects.filter(status="Active")

    @staticmethod
    def search_employees(keyword):
        """
        Search employees by name, employee number,
        username or national ID.
        """
        return Employee.objects.filter(
            user__first_name__icontains=keyword
        ) | Employee.objects.filter(
            user__last_name__icontains=keyword
        ) | Employee.objects.filter(
            employee_number__icontains=keyword
        ) | Employee.objects.filter(
            national_id__icontains=keyword
        )