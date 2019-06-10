from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class NormalUserForm(UserCreationForm):
    StudentID = forms.CharField(required=True, max_length=10)
    Phone = forms.CharField(required=True, max_length=11)
    Gender = forms.CharField(max_length=1)

    class Meta:
        model = User
        fields = ("username", "email", "StudentID", "Phone", "Gender", "password1", "password2",)
