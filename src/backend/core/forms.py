from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from .models import *

class PersonalAccountSignupForm(UserCreationForm):
    pass

class CompanyAccountSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['first_name', 'username', 'password1', 'password2']
