from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def Game(request):
    return render(request, "Game.html")
def Game2(request):
    return render(request, "Game2.html")