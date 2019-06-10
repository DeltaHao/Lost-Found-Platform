from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User


class NormalUserChangeForm(UserChangeForm):
    StudentID = forms.CharField(required=True, max_length=10)
    Phone = forms.CharField(required=True, max_length=11)
    Gender = forms.CharField(max_length=1)

    class Meta:
        model = User
        fields = ("username", "email", "StudentID", "Phone", "Gender", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NormalUserForm(UserCreationForm):
    StudentID = forms.CharField(required=True, max_length=10)
    Phone = forms.CharField(required=True, max_length=11)
    Gender = forms.CharField(max_length=1)

    class Meta:
        model = User
        fields = ("username", "email", "StudentID", "Phone", "Gender", "password1", "password2",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)





