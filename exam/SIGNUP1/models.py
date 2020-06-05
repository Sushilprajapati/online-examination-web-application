from django.db import models
from datetime import datetime
import datetime

class My_Student1(models.Model):
    s_id = models.CharField(primary_key=True,max_length=15, null=False,unique=True)
    s_name = models.CharField(max_length=20,null=False)
    course = models.CharField(max_length=20,null=False)
    semester = models.IntegerField(null=False)
    DOB = models.DateField()
    Email = models.CharField(max_length=40,unique=True)
    Phone = models.CharField(max_length=12,unique=True)
    status = models.BooleanField()
# for show id in /admin
def __str__(self):
    return self.s_id

#other add , student submisssion
class Student_signup_record1(models.Model):
    college_id = models.CharField(primary_key=True,max_length=15,unique=True)
    s_name = models.CharField(max_length=20,null=False)
    semester = models.IntegerField()
    email = models.CharField(max_length=40,unique=True,null=False)
    password = models.CharField(max_length=15,default=0)
   # date = models.DateTimeField(auto_now_add=True)
#for show id in /admin
def __str__(self):
    return self.college_id
