from django.contrib.auth.models import User as DjangoUser
from django.db import models

class PersonalAccountEducation(models.Model):
    education = models.TextField(max_length=250)

class PersonalAccountCert(models.Model):
    cert_name = models.TextField(max_length=70)

class PersonalAccountSkill(models.Model):
    skill = models.TextField(max_length=70)

class PersonalAccount(DjangoUser):
    education = models.ManyToManyField(PersonalAccountEducation)
    certs = models.ManyToManyField(PersonalAccountCert)  

class CompanyAccount(DjangoUser):
    contact_number = models.IntegerField()

class PersonalAccountPost(models.Model):
    title = models.TextField(max_length=70)
    body = models.TextField(max_length=200)
    disable_reactions = models.BooleanField(default=False)
    disable_comments = models.BooleanField(default=False)

class PersonalAccountReaction(models.Model):
    reactor = models.ForeignKey(PersonalAccount, on_delete=models.CASCADE)
    post = models.ForeignKey(PersonalAccountPost, on_delete=models.CASCADE)

class PersonalAccountComment(models.Model):
    commentor = models.ForeignKey(PersonalAccount, on_delete=models.CASCADE \
            related_name='comments')
    post = models.ForeignKey(PersonalAccountPost, on_delete=models.CASCADE \
            related_name='comments')
    text = models.TextField(max_length=200)

class JobPost(models.Model):
    poster = models.ForeignKey(CompanyAccount, on_delete=models.CASCADE)
    job_title = models.TextField(max_length=70)
    description = models.TextField(max_length=3000)
    max_salary = models.PositiveIntegerField()
    min_salary = models.PositiveIntegerField()
    required_skills = models.ManyToManyField(PersonalAccountSkill)
    required_education = models.ForeignKey(PersonalAccountEducation, null=True, on_delete=models.SET_NULL)
    required_certificates = models.ManyToManyField(PersonalAccountCert)

