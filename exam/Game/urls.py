from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   path('Game', views.Game, name="game"),
   path('Game2', views.Game2, name="game2"),


]