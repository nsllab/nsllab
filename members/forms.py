# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Member

class MemberCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)

        # Set is_active to False for all users except is_staff=True
        if not user.is_staff:
            user.is_active = False

        if commit:
            user.save()

        return user

class MemberUpdateForm(UserChangeForm):
    class Meta:
        model = Member
        fields = ['username', 'first_name', 'last_name', 'email']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)