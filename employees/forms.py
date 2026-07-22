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
            "user": forms.Select(attrs={"class": "form-select"}),
            "gender": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "date_of_birth": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "hire_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "address": forms.Textarea(
                attrs={"rows": 3, "class": "form-control"}
            ),
            "profile_photo": forms.FileInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Dynamically attach form-control / form-select to all fields safely
        for field in self.fields.values():
            if isinstance(field.widget, forms.Select):
                existing_class = field.widget.attrs.get("class", "")
                if "form-select" not in existing_class:
                    field.widget.attrs["class"] = f"{existing_class} form-select".strip()
            else:
                existing_class = field.widget.attrs.get("class", "")
                if "form-control" not in existing_class:
                    field.widget.attrs["class"] = f"{existing_class} form-control".strip()

    def clean_employee_number(self):
        employee_number = self.cleaned_data.get("employee_number")

        qs = Employee.objects.filter(employee_number=employee_number)
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError(
                "Employee number already exists."
            )

        return employee_number

    def clean_national_id(self):
        national_id = self.cleaned_data.get("national_id")

        qs = Employee.objects.filter(national_id=national_id)
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
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
            "gender": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "date_of_birth": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "hire_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "address": forms.Textarea(
                attrs={"rows": 3, "class": "form-control"}
            ),
            "profile_photo": forms.FileInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if isinstance(field.widget, forms.Select):
                existing_class = field.widget.attrs.get("class", "")
                if "form-select" not in existing_class:
                    field.widget.attrs["class"] = f"{existing_class} form-select".strip()
            else:
                existing_class = field.widget.attrs.get("class", "")
                if "form-control" not in existing_class:
                    field.widget.attrs["class"] = f"{existing_class} form-control".strip()

    def clean_national_id(self):
        national_id = self.cleaned_data.get("national_id")

        if Employee.objects.filter(
            national_id=national_id
        ).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                "National ID already exists."
            )

        return national_id