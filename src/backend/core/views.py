from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpRequest
from django.db.models import Q
from .models import *
from .forms import *

def index(req: HttpRequest):
    user_profile, _ = get_user_profile(req.user)

    form = None
    if user_profile == 'personal':
        form = PersonalAccountPostForm()

    elif user_profile == 'company':
        form = JobPostForm()

    context = { 'profile': user_profile, 
               'user': req.user, 
               'form': form,
               'search_results': None,
    }

    return render(req, 'core/index.html', context)

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
        signup_form = PersonalAccountSignupForm(req.POST)
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

        _, poster = get_user_profile(req.user)
        post_form = PersonalAccountPostForm(req.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.poster = poster
            post.save()
        
        return redirect(reverse('core:index'))


def jobpost(req: HttpRequest, pk=-1):

    user_profile, profile_obj = get_user_profile(req.user)

    if req.method == 'GET':
        jobpost = get_object_or_404(JobPost, pk=pk)
        return render(req, 'core/jobpost.html', {'user_profile': user_profile, 'jobpost': jobpost })

    elif req.method == 'POST' and user_profile == 'personal':
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

def personal_profile(req: HttpRequest, is_self, pk=-1):
    user = get_object_or_404(PersonalAccount, pk=req.user.id if is_self else pk)
    is_self = is_self or user.user == req.user
    add_skill_form = AddSkillForm(user) if is_self else None
    return render(req, 'core/personal_profile.html', {'user': user, 'is_self': is_self, 'add_skill_form': add_skill_form})

def add_skill(req: HttpRequest):
    if not req.user.is_authenticated:
        return redirect(reverse('core:personal_login'))

    if req.method != 'POST':
        # TODO: raise an error
        return redirect(reverse('core:index'))
    
    profile_type, profile = get_user_profile(req.user)

    if profile_type != 'personal':
        # TODO: raise an error
        return redirect(reverse('core:index'))

    skill_form = AddSkillForm(profile, req.POST)

    if skill_form.is_valid():
        skill = skill_form.cleaned_data['skill']
        skill = PersonalAccountSkill.objects.get(skill=skill)
        profile.skills.add(skill)
        profile.save()

        return redirect(reverse('core:personal_profile_self'))

    return redirect(reverse('core:personal_profile_self'))

def search_jobposts(req: HttpRequest):
    user_profile, _ = get_user_profile(req.user)

    form = None
    if user_profile == 'personal':
        form = PersonalAccountPostForm()

    elif user_profile == 'company':
        form = JobPostForm()

    search_query = req.GET['query']
    search_result = JobPost.objects.filter(Q(job_title__icontains=search_query) | Q(description__icontains=search_query))

    context = { 'profile': user_profile, 
               'user': req.user, 
               'form': form,
               'search_results': search_result,
   }

    return render(req, 'core/index.html', context)


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

    return user_type, user_obj

