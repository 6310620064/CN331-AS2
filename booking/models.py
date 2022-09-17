from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    code = models.CharField(max_length=5, unique=True)
    subject_name = models.CharField(max_length=64)
    semester = models.CharField(max_length=1)
    academic_year = models.CharField(max_length=4)
    quota = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    student = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{ self.code }  { self.subject_name }'

class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='Subject')
    
    def __str__(self):
        return f'{ self.user } { self.subject }'
