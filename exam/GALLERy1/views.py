from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def gallery1(request):
    from .models import User
    users = User.objects.all()
    p = users[len(users)-1].pic
    print(p.url)
    return render(request, 'gallery1.html',{'users':users})

def upload(request):
    print("this is work proprley ")
    p = request.FILES['image'];
    from .models import User
    user = User(pic = p);
    user.save()
    return render(request, 'gallery1.html')