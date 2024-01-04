from django.urls import path
from .views import *
from functools import partial

app_name = 'core'
urlpatterns = [
        path('', index, name='index'),
        path('login/personal', personal_login, name='personal_login'),
        path('login/company', company_login, name='company_login'),
        path('signup/personal', personal_signup, name='personal_signup'),
        path('signup/company', company_signup, name='company_signup'),
        
]
