from django.shortcuts import render,HttpResponse,redirect
from .models import IMG_STORE
import pyautogui as pg

# Create your views here.
def gallery(request):
    return render(request,"gallery.html")

def add_img(request):
    if request.method == 'POST':
        p = request.POST.get('image')
        d = IMG_STORE(pic = p)
        # print("jdgjkdgjdkgdkgj ---------" , d)
        d.save()
        # #pg.alert("Upload Done")
        # print("\n\n hello \n\n ")
        d = IMG_STORE.objects.all()
        # r = d[len(d) - 1].pic
        # print("urls is ======== " + r.url)
        # print(d)
            # print()
        return render(request, 'gallery.html',{'d':d})
# def up(request):
#     print("\n susjhdfgjhsgfh hdgfhdsgfh \n")
#     return render(request,'gallery.html')
