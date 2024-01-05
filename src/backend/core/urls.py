from django.urls import path
from .views import *
from functools import partial

app_name = 'core'
urlpatterns = [
        path('', index, name='index'),
        path('logout', logout_, name='logout'),
        path('login/personal', personal_login, name='personal_login'),
        path('login/company', company_login, name='company_login'),
        path('signup/personal', personal_signup, name='personal_signup'),
        path('signup/company', company_signup, name='company_signup'),
        path('post', post, name='post'),
        path('post/<int:pk>', post, name='post'),
        path('jobpost', jobpost, name='jobpost'),
        path('jobpost/<int:pk>', jobpost, name='jobpost'),
        path('personal/<int:pk>', partial(personal_profile, is_self=False), name='personal_profile'),
        path('personal/profile', partial(personal_profile, is_self=True), name='personal_profile_self'),
        path('personal/add_skill', add_skill, name='add_skill'),
]

