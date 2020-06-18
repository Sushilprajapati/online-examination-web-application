from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
         path('gallery', views.gallery, name="gallery_page"),
         path('add_img', views.add_img, name="galler"),
       #  path('gallery', views.up,name="hdfjd"),
   # path('up', views.up, name="gallery_page"),
    #path('gallery', views.login1, name="login_page1"),
    ]