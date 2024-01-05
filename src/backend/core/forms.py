from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from .models import *

class PersonalAccountSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class CompanyAccountSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['first_name', 'email', 'username', 'password1', 'password2']

class PersonalAccountPostForm(forms.ModelForm):
    class Meta:
        model = PersonalAccountPost
        fields = ['title', 'body']
        widgets = {
                'title': forms.TextInput()
        }

