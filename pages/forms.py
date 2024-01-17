from django import forms
from .models import Serendipity

class SerendipityForm(forms.ModelForm):
    class Meta:
        model = Serendipity
        fields = ['subject']

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     instance.writer = self.writer  # Assuming you have a 'user' field in your MyModel
    #     if commit:
    #         instance.save()
    #     return instance
