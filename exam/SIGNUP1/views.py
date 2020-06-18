from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
import pyautogui as pg
from .models import Student_signup_record1,My_Student1,one_time_access_check
from django.contrib.auth import authenticate, login

from django.contrib.auth import authenticate
from django.contrib import  messages
# Create your views here.
def signup(request):
     return render(request,"signup.html")


def exam(request):
    if request.method == 'POST':
        signup_College_Id = request.POST.get("signup_College_Id")
        signup_college_name = request.POST.get('signup_college_name',False)
        semester = request.POST.get('semester',False)
        signup_email = request.POST.get('signup_email',False)
        signup_password = request.POST.get('signup_password',False)

        signup_College_Id.upper();
        signup_college_name.upper();
      # check is alreday member  or not
        if User.objects.filter(username = signup_College_Id).exists():
            pg.alert("User already exist")
            return render(request, "signup.html")
        else:
            x =  Student_signup_record1( college_id = signup_College_Id,s_name = signup_college_name, password = signup_password, email =  signup_email,semester =semester )
            x.save()

           # s = My_Student1.objects.all().filter(s_id = signup_College_Id);
            #print(s)

            # check this user is exist in my list or not
            if not My_Student1.objects.filter(s_id= signup_College_Id, s_name=signup_college_name).exists():
                pg.alert("Please, Enter valied college id and college name")
                return render(request, "signup.html")
            else:
        #for create user
                u = User.objects.create_user(username=signup_College_Id,password= signup_password,email=signup_email)
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
        login_college_id = request.POST['login_college_id']
        login_password = request.POST['login_password']
        from django.contrib import auth
        user = authenticate(request,username = login_college_id, password = login_password)
       # user = Student_signup_record1.objects.filter(College_id = login_college_id).exists()
        #print(college_idl, password)
        if user is  None:
            pg.alert("Wrong Id or Password ")
            return render(request, 'login.html')
        else:
            return render(request, "exam.html")
# for check exam submit or not
def bsccs(request):
    username = request.user.username
    if one_time_access_check.objects.filter( access_check_status  = 1).exists():
        pg.alert("You are already submit exam")
        return redirect('/')
    else:
        y = one_time_access_check(student_id_user = username,  access_check_status  = 1)
        y.save()
        return render(request,'examform.html')

