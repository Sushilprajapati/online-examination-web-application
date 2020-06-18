from django.shortcuts import render,HttpResponse,redirect
from .models import IMG_STORE

# Create your views here.
def gallery(request):
    return render(request,"gallery.html")

def add(request):
    if request.method == 'POST':
        p = request.FILES['image']
        d = IMG_STORE(img_add = p)
        d.save()
    # return render(request, 'login.html')
def up(request):
    return render(request,'login.html')
