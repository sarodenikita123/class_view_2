from django import forms
from .models import Exam


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = "__all__"

        widgets = {
            "college_name": forms.TextInput(attrs={"class": "form-control"}),
            "candidate_name": forms.TextInput(attrs={"class": "form-control"}),
            "mother_name": forms.TextInput(attrs={"class": "form-control"}),
            "father_name": forms.TextInput(attrs={"class": "form-control"}),
            "exam_name": forms.TextInput(attrs={"class": "form-control"}),
            "center": forms.TextInput(attrs={"class": "form-control"}),
        }
