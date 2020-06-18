from django.db import models

# Create your models here.
class IMG_STORE(models.Model):
    pic = models.ImageField(upload_to="photos", blank=True,default='')

