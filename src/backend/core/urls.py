from django.urls import path
from .views import *
from functools import partial

app_name = 'core'
urlpatterns = [
        path('', index),
        path('login/personal', personal_login, name='personal_login'),
        path('login/company', company_login, name='company_login'),
]

