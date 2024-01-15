from django import forms
from .models import WeeklyReport

class WeeklyReportForm(forms.ModelForm):
    class Meta:
        model = WeeklyReport
        exclude = ['user', 'writer']