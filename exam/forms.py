# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import *

class BaseForm(forms.ModelForm):

    class Meta:
        model = ExamTr
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label 
            field.widget.attrs['onkeyup'] = "this.setAttribute('value', this.value);"
            field.widget.attrs['value'] = ""
            field.label = ''


class ConfigForm(BaseForm):

    class Meta:
        model = ExamTr
        fields = (
            "volume",
            "scope",
            "year",
        )


class ExamForm(BaseForm):

    class Meta:
        model = ExamTr
        fields = (
            "questions",
            "answers",
        )


class ResultForm(BaseForm):

    class Meta:
        model = ExamTr
        fields = (
            "questions",
            "answers",
        )


class ReportForm(BaseForm):

    class Meta:
        model = ExamTr
        fields = (
            "questions",
            "answers",
        )
