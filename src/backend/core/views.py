from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpRequest
from .models import *
from .forms import *

def index(req: HttpRequest):
    user_profile, _ = get_user_profile(req.user)

    form = None
    if user_profile == 'personal':
        form = PersonalAccountPostForm()

    elif user_profile == 'company':
        form = JobPostForm()

    return render(req, 'core/index.html', {'profile': user_profile, 'user': req.user, 'form': form })

def logout_(req: HttpRequest):
    logout(req)
    return redirect(reverse('core:index'))

def personal_login(req: HttpRequest):
    if req.user.is_authenticated:
        return redirect(reverse('core:index'))

    login_form = None
    if req.method == 'POST':
        login_form = AuthenticationForm(req, req.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(req, user)
            return redirect(reverse('core:index'))

    return render(req, 'core/login.html', {'form': login_form or AuthenticationForm() })

def company_login(req: HttpRequest):
    if req.user.is_authenticated:
        return redirect(reverse('core:index'))

    login_form = None
    if req.method == 'POST':
        login_form = AuthenticationForm(req, req.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(req, user)
            return redirect(reverse('core:index'))

    return render(req, 'core/login.html', {'type': 'company', 'form': login_form or AuthenticationForm() })

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
    if req.user.is_authenticated:
        return redirect(reverse('core:index'))

    signup_form = None

    if req.method == 'POST':
        signup_form = UserCreationForm(req.POST)
        if signup_form.is_valid():
            new_user = signup_form.save()
            new_company_profile = CompanyAccount.objects.create(user=new_user)
            new_company_profile.save()
            login(req, new_user)

            return redirect(reverse('core:index'))
    return render(req, 'core/signup.html', { 'type': 'company', 'form': signup_form or CompanyAccountSignupForm() })

def post(req: HttpRequest, pk=-1):
    if req.method == 'GET':
        post = get_object_or_404(PersonalAccountPost, pk=pk)
        return render(req, 'core/post.html', {'post': post})

    elif req.method == 'POST':
        if not req.user.is_authenticated:
            return redirect(reverse('core:personal_login'))
        post_form = PersonalAccountPostForm(req.POST)
        if post_form.is_valid():
            post_form.save(commit=True)
        
        return redirect(reverse('core:index'))


def jobpost(req: HttpRequest, pk=-1):

    user_profile, profile_obj = get_user_profile(req.user)

    if req.method == 'GET':
        jobpost = get_object_or_404(JobPost, pk=pk)
        return render(req, 'core/jobpost.html', {'user_profile': user_profile, 'jobpost': jobpost })

    elif req.method == 'POST' and user_profile == 'personal':
        print("applying to ", req.POST['jobpost_id'])
        jobpost = get_object_or_404(JobPost, pk=req.POST['jobpost_id'])
        try:
            JobPostApplication.objects.get(jobpost=jobpost, applicant=profile_obj)

        except JobPostApplication.DoesNotExist:
            application = JobPostApplication.objects.create(jobpost=jobpost, applicant=profile_obj)
            application.save()

        return redirect(reverse('core:index'))

    elif req.method == 'POST' and user_profile == 'company':
        jobpost_form = JobPostForm(req.POST)
        if jobpost_form.is_valid():
            jobpost = jobpost_form.instance.poster = profile_obj
            jobpost_form.save()
            return redirect(reverse('core:index'))

        return render(req, 'core/jobpost.html', {'user_profile': user_profile, 'jobpost_form': jobpost_form })

def get_user_profile(user):
    user_type = ''
    user_obj = None
    got_user = False

    if user.is_authenticated:
        try:
            user_obj = PersonalAccount.objects.get(user=user)
            user_type = 'personal'
            got_user = True
        except PersonalAccount.DoesNotExist:
            pass

        if not got_user:
            try:
                user_obj = CompanyAccount.objects.get(user=user)
                user_type = 'company'
            except CompanyAccount.DoesNoExist:
                pass

    return (user_type, user_obj)

