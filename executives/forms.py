from django import forms
from .models import *


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = "__all__"


class DirectorateForm(forms.ModelForm):
    class Meta:
        model = Directorate
        fields = "__all__"
