from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from .models import Student_signup_record1
from django.contrib.auth import authenticate
# Create your views here.
def signup(request):
     return render(request,"signup.html")


def exam(request):
    if request.method == 'POST':
        signup_College_Id = request.POST.get("signup_College_Id")
        signup_college_name = request.POST.get('signup_college_name',False)
        semester = request.POST.get('semester',False)
        signup_email = request.POST.get('signup_email',False)
        signup_password = request.POST.get('signup_password',False)       #
        x =  Student_signup_record1( college_id = signup_College_Id,s_name = signup_college_name, password = signup_password, email =  signup_email,semester =semester )
        x.save()
        #for create user
        u = User(username=signup_College_Id,email=signup_email,password= signup_password)
        u.save()
        return render(request, "exam.html")
    else:
       return redirect('/')



# go to tlogin page
def login(request):
    return render(request, "login.html")



# login system + create user

def loginexam(request):
    if request.method == 'POST':
        login_college_id = request.POST.get('login_college_id',False)
        login_password = request.POST.get('login_password',False)
        from django.contrib import auth
        user = authenticate(username = login_college_id, password = login_password)

        #print(college_idl, password)
        if user is not None:
            return render(request, 'login.html')
        else:
            return render(request, "exam.html")