from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def gallery(request):
    return render(request,"gallery.html")
