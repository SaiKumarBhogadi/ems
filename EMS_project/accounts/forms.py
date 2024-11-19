from django import forms
from django.contrib.auth.models import User #We are using built-in user 'model' from 'auth' module
from django.contrib.auth.forms import UserCreationForm #We are using built-in 'form' from 'auth' module

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']