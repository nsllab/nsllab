from django import forms
from .models import WeeklyReport, PostDocReport

class WeeklyReportForm(forms.ModelForm):
    class Meta:
        model = WeeklyReport
        exclude = ['user', 'writer']

class PostDocReportForm(forms.ModelForm):
    class Meta:
        model = PostDocReport
        exclude = ['users', 'writer']