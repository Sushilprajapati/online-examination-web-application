from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
         path('gallery', views.gallery, name="gallery_page"),
         path('image_g', views.add, name="galler"),
        path('gellery', views.up,name="hdfjd"),
    ]