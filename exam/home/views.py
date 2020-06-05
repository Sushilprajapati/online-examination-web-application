from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def homepage(request):
    return render(request,"Home.html")

