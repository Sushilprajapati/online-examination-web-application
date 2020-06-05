from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def about(request):
     return render(request,"about.html")