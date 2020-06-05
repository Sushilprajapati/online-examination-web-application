from django.db import models

# Create your models here.

from django.db import models
from . import views
# me add
# class My_Student(models.Model):
#     s_id = models.CharField(primary_key=True,max_length=15, null=False,unique=True)
#     s_name = models.CharField(max_length=20,null=False)
#     course = models.CharField(max_length=20,null=False)
#     semester = models.IntegerField(null=False)
#     DOB = models.DateField()
#     Email = models.CharField(max_length=40,unique=True)
#     Phone = models.CharField(max_length=12,unique=True)
#     status = models.BooleanField()
#
# #other add , student submisssion
# class Student_signup_record(models.Model):
#     college_id = models.CharField(primary_key=True,max_length=15, null=False,unique=True)
#     s_name = models.CharField(max_length=20,null=False)
#     semester = models.IntegerField(null=False)
#     email = models.CharField(max_length=40,unique=True)
#     password = models.CharField(max_length=15)





