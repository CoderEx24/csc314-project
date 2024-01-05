from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.http import HttpRequest
from .models import *
from .forms import *

def index(req: HttpRequest):
    print(req.user)
    return render(req, 'core/index.html', { 'user': req.user })

def logout_(req: HttpRequest):
    logout(req)
    return redirect(reverse('core:index'))

def personal_login(req: HttpRequest):
    if req.method == 'GET':
        return render(req, 'core/login.html', {'form': AuthenticationForm() })
    elif req.method == 'POST':
        login_form = AuthenticationForm(req.data)
        if login_form.is_valid():
            return render(req, 'core/index.html', {'user': req.user })

        return render(req, 'core/login.html', {'form': login_form })

def company_login(req: HttpRequest):
    if req.method == 'GET':
        return render(req, 'core/login.html', {'form': AuthenticationForm() })
    elif req.method == 'POST':
        login_form = AuthenticationForm(req.data)
        if login_form.is_valid():
            return render(req, 'core/index.html', {'user': req.user })

        return render(req, 'core/login.html', {'form': login_form })

def personal_signup(req: HttpRequest):
    if req.user.is_authenticated:
        return redirect(reverse('core:index'))

    signup_form = None

    if req.method == 'POST':
        signup_form = UserCreationForm(req.POST)
        if signup_form.is_valid():
            new_user = signup_form.save()
            new_personal_profile = PersonalAccount.objects.create(user=new_user)
            new_personal_profile.save()
            login(req, new_user)
            return redirect(reverse('core:index'))

    return render(req, 'core/signup.html', { 'form': signup_form or PersonalAccountSignupForm() })

def company_signup(req: HttpRequest):
    if req.method == 'POST':
        signup_form = UserCreationForm(req.POST)
        if signup_form.is_valid():
            new_user = signup_form.save()
            new_company_profile = CompanyAccount.objects.create(user=new_user)
            new_company_profile.save()
            login(req, new_user)

            return redirect(reverse('core:index'))
    return render(req, 'core/signup.html', { 'type': 'company', 'form': CompanyAccountSignupForm() })

