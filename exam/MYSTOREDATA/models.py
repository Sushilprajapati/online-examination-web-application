from django.db import models

# Create your models here.
class Fill_Student(models.Model):
    s_id = models.CharField(primary_key=True,max_length=15)
    s_name = models.CharField(max_length=20)
    DOB = models.DateField()
    Email = models.CharField(max_length=40)
    Phone = models.IntegerField(max_length=10)
    status = models.BooleanField();
