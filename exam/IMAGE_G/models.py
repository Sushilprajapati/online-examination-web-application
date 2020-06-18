from django.db import models

# Create your models here.
class IMG_STORE(models.Model):
    img_add = models.ImageField(upload_to="pics", blank=True)

