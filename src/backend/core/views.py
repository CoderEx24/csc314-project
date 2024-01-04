from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from django.http import HttpRequest
from .models import *
from .forms import *

def index(req: HttpRequest):
    print(req.user)
    return render(req, 'core/index.html', { 'user': req.user })

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


