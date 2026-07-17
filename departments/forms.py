from django import forms

from .models import Department


class DepartmentForm(forms.ModelForm):
    """
    Form for creating a department.
    """

    class Meta:
        model = Department

        fields = [
            "department_name",
            "department_code",
            "manager",
            "email",
            "phone_number",
            "location",
            "description",
            "is_active",
        ]

        widgets = {
            "department_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Department Name",
                }
            ),

            "department_code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Department Code",
                }
            ),

            "manager": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Department Email",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone Number",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Office Location",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Department Description",
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

    def clean_department_name(self):
        department_name = self.cleaned_data["department_name"]

        if Department.objects.filter(
            department_name__iexact=department_name
        ).exists():
            raise forms.ValidationError(
                "A department with this name already exists."
            )

        return department_name

    def clean_department_code(self):
        department_code = self.cleaned_data["department_code"]

        if Department.objects.filter(
            department_code__iexact=department_code
        ).exists():
            raise forms.ValidationError(
                "A department with this code already exists."
            )

        return department_code


class DepartmentUpdateForm(forms.ModelForm):
    """
    Form for updating a department.
    """

    class Meta:
        model = Department

        fields = [
            "department_name",
            "department_code",
            "manager",
            "email",
            "phone_number",
            "location",
            "description",
            "is_active",
        ]

        widgets = {
            "department_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "department_code": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "manager": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

    def clean_department_name(self):
        department_name = self.cleaned_data["department_name"]

        if Department.objects.filter(
            department_name__iexact=department_name
        ).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                "A department with this name already exists."
            )

        return department_name

    def clean_department_code(self):
        department_code = self.cleaned_data["department_code"]

        if Department.objects.filter(
            department_code__iexact=department_code
        ).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                "A department with this code already exists."
            )

        return department_code