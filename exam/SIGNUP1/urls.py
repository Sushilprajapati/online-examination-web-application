from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path('signup', views.signup, name="signup"),
   path('exam',views.exam,name = "exam_page"),
   path('login', views.login, name="login_page"),
   path('exam', views.loginexam, name="login_exam_page"),
]