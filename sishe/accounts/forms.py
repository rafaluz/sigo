from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','email', 'password1','password2']