from django import forms
from django.utils import timezone

from .models import Task


class TaskForm(forms.ModelForm):
    """
    Form for creating a task.
    """

    class Meta:
        model = Task

        exclude = (
            "assigned_by",
            "completed_date",
            "created_at",
            "updated_at",
        )

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Task Title",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Task Description",
                }
            ),

            "assigned_to": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "priority": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "progress": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                    "max": 100,
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "due_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Additional Remarks",
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        start_date = cleaned_data.get("start_date")
        due_date = cleaned_data.get("due_date")
        progress = cleaned_data.get("progress")

        if start_date and due_date:
            if due_date < start_date:
                raise forms.ValidationError(
                    "Due date cannot be earlier than the start date."
                )

        if start_date:
            if start_date < timezone.now().date():
                raise forms.ValidationError(
                    "Start date cannot be in the past."
                )

        if progress is not None:
            if progress < 0 or progress > 100:
                raise forms.ValidationError(
                    "Progress must be between 0 and 100."
                )

        return cleaned_data


class TaskUpdateForm(forms.ModelForm):
    """
    Form for updating a task.
    """

    class Meta:
        model = Task

        exclude = (
            "assigned_by",
            "created_at",
            "updated_at",
        )

        widgets = {

            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                }
            ),

            "assigned_to": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "priority": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "progress": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                    "max": 100,
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "due_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "completed_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        start_date = cleaned_data.get("start_date")
        due_date = cleaned_data.get("due_date")
        completed_date = cleaned_data.get("completed_date")
        progress = cleaned_data.get("progress")

        if start_date and due_date:
            if due_date < start_date:
                raise forms.ValidationError(
                    "Due date cannot be earlier than the start date."
                )

        if completed_date and due_date:
            if completed_date < start_date:
                raise forms.ValidationError(
                    "Completion date cannot be earlier than the start date."
                )

        if progress is not None:
            if progress < 0 or progress > 100:
                raise forms.ValidationError(
                    "Progress must be between 0 and 100."
                )

        return cleaned_data