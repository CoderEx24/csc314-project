from rest_framework.serializers import ModelSerializer \
    as ModelSerialiser
from ..core.models import *

class PersonalAccountSerialiser(ModelSerialiser):
    class Meta:
        model = PersonalAccount
        fields = ['username', 'education', 'certs']

class CompanyAccountSerialiser(ModelSerialiser):
    class Meta:
        model = CompanyAccount
        fields = ['username', 'contact_number']

class PersonalAccountPostSerialiser(ModelSerialiser):
    class Meta:
        model = PersonalAccountPost
        fields = ['title', 'body', 'disable_reactions',
                  'disable_comments', 'comments']

class JobPostSeraliser(ModelSerialiser):
    class Meta:
        model = JobPost
        fields = '__all__'

