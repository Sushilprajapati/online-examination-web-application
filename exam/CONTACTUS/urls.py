from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path('contactus', views.contactus, name="contactus_page"),
]