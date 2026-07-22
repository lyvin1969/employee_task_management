from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    """
    Form for creating a new employee.
    """

    class Meta:
        model = Employee

        fields = [
            "user",
            "employee_number",
            "phone_number",
            "national_id",
            "gender",
            "date_of_birth",
            "address",
            "job_title",
            "hire_date",
            "profile_photo",
            "status",
            "emergency_contact_name",
            "emergency_contact_phone",
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'hire_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if not isinstance(field.widget, forms.DateInput):
                field.widget.attrs["class"] = "form-control"

    def clean_employee_number(self):
        employee_number = self.cleaned_data["employee_number"]

        if Employee.objects.filter(
            employee_number=employee_number
        ).exists():
            raise forms.ValidationError(
                "Employee number already exists."
            )

        return employee_number

    def clean_national_id(self):
        national_id = self.cleaned_data["national_id"]

        if Employee.objects.filter(
            national_id=national_id
        ).exists():
            raise forms.ValidationError(
                "National ID already exists."
            )

        return national_id


class EmployeeUpdateForm(forms.ModelForm):
    """
    Form for updating employee details.
    """

    class Meta:
        model = Employee

        fields = [
            "phone_number",
            "national_id",
            "gender",
            "date_of_birth",
            "address",
            "job_title",
            "hire_date",
            "profile_photo",
            "status",
            "emergency_contact_name",
            "emergency_contact_phone",
        ]

        widgets = {
            "date_of_birth": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "hire_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "address": forms.Textarea(
                attrs={"rows": 3, "class": "form-control"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if not isinstance(field.widget, forms.DateInput):
                field.widget.attrs["class"] = "form-control"

    def clean_national_id(self):
        national_id = self.cleaned_data["national_id"]

        if Employee.objects.filter(
            national_id=national_id
        ).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                "National ID already exists."
            )

        return national_id