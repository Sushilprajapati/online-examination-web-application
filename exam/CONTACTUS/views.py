from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def contactus(request):
    return render(request,'contactus.html')

