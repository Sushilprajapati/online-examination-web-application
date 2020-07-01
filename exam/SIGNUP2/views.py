import time
import pyautogui as pg
import pyscreenshot as ImageGrab
import PIL
from django.contrib.auth.models import User
import re
from django.shortcuts import render, HttpResponse, redirect
import pyautogui as pg
from .models import My_Student1,one_time_access_check,Student_signup_record1,Exam_result
# Student_signup,,Student_signup_r
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate
from django.contrib import  messages
from threading import Thread
import sys
takescreen = 0
stop_screenshort = 0

#take screenshort after some time
def Takescreenshort():
    global stop_screenshort
    k = 0
    while True:
        if stop_screenshort == 1:
            return
        else:
            time.sleep(5)
            image = ImageGrab.grab()
            im = ImageGrab.grab(bbox=(200, 10, 1600, 500))
            im = im.save("/home/sushil/Desktop/o.png")
            print("hold_user")
            # k = k + 1
            # stop_screenshort = stop_screenshort + 1


# for show current page according to user
def matchuser(request, id):
    if (re.findall('BCSS2018', id)):
        #while True:
        #Takescreenshort()
        return render(request, "exam.html")

    elif (re.findall('BCSS2019', id)):
        return render(request, "about.html")
    elif (re.findall('BCSS2017', id)):
        return render(request, "exam.html")
    else:
        return render(request, "exam.html")

# Create your views here.
def signup(request):
     return render(request,"signup.html")

hold_user  = "hello_user"
#semester = 1
def exam(request):
    if request.method == 'POST':
        global hold_user
 #       global semester
        signup_College_Id = request.POST.get("signup_College_Id")
        signup_college_name = request.POST.get('signup_college_name',False)
        semester = request.POST.get('semester',False)
        signup_date = request.POST.get('signup_date',False)
        signup_password = request.POST.get('signup_password',False)
        hold_user = request.POST.get("signup_College_Id")
        semester = request.POST.get('semester',False)
        signup_College_Id.upper();
        signup_college_name.upper();
      # check is alreday member  or not
        if User.objects.filter(username = signup_College_Id).exists():
            pg.alert("User already exist")
            return render(request, "signup.html")
        else:
            x =  Student_signup_record1( college_id = signup_College_Id,s_name = signup_college_name, password = signup_password, D_O_B =  signup_date,semester =semester )
            x.save()

           # s = My_Student1.objects.all().filter(s_id = signup_College_Id);
            #print(s)

            # check this user is exist in my list or not
            if not My_Student1.objects.filter(s_id= signup_College_Id, s_name=signup_college_name,DOB = signup_date).exists():
                pg.alert("Please, Enter valied college id and college name")
                return render(request, "signup.html")
            else:
        #for create user
                u = User.objects.create_user(username=signup_College_Id,password= signup_password,email= signup_college_name)
                u.save()
                return matchuser(request, hold_user)
                #return render(request, "exam.html")
    else:
       return redirect('/')







# go to tlogin page
def login(request):
    return render(request, "login.html")



# login system + create user

def loginexam(request):
    if request.method == 'POST':
        global hold_user
        global semester
        login_college_id = request.POST['login_college_id']
        login_password = request.POST['login_password']
        hold_user = request.POST['login_college_id']
        from django.contrib import auth
        user = authenticate(request,username = login_college_id, password = login_password)
       # user = Student_signup_record1.objects.filter(College_id = login_college_id).exists()
        #print(college_idl, password)
        if user is  None:
            pg.alert("Wrong Id or Password ")
            return render(request, 'login.html')
        else:
            return matchuser(request, hold_user)

            #return render(request, "exam.html")
            #return render(request,"signup.html")

# for check exam submit or not
def bsccs(request):
    global takescreen
    global hold_user
    global stop_screenshort
    takescreen = 1
    # username = request.user.username
    # user = authenticate(request, username=login_college_id, password=login_password)
    users = User.objects.all()
    print(users)
    if one_time_access_check.objects.filter(student_id_user = hold_user, access_check_status  = 1).exists():
        pg.alert("You are already submit exam")
        return redirect('/')
    else:
        print(hold_user)
        y = one_time_access_check(student_id_user = hold_user,  access_check_status  = 1)
        y.save()
        #try:
        # return render(request, 'examform.html', {'showidonpage': hold_user})

           # return render(request, 'examform.html', {'showidonpage': hold_user})
        #finally:
       #   Takescreenshort()

        t = Thread(target= Takescreenshort)
        t.start()
        # if stop_screenshort == 1:
        #     sys.exit()

        return render(request,'examform.html',{'showidonpage':hold_user})

      #  Takescreenshort()

def Examformsubmit(request):
    if request.method == 'POST':
        global stop_screenshort
        global hold_user
        stop_screenshort = 1
        print("sushil ")
        # True False result
        ecomerrce000 = request.POST.get("ecomerrce000")
        ecomerrce001 = request.POST.get("ecomerrce001")
        ecomerrce002 = request.POST.get("ecomerrce002")
        ecomerrce003 = request.POST.get("ecomerrce003")
        ecomerrce004 = request.POST.get("ecomerrce004")
        ecomerrce005 = request.POST.get("ecomerrce005")
        ecomerrce006 = request.POST.get("ecomerrce006")
        ecomerrce007 = request.POST.get("ecomerrce007")
        ecomerrce008 = request.POST.get("ecomerrce008")
        ecomerrce009 = request.POST.get("ecomerrce009")
        # Multiple choiece result
        ecomerrce1 = request.POST.get("ecomerrce1")
        ecomerrce2 = request.POST.get("ecomerrce2")
        ecomerrce3 = request.POST.get("ecomerrce3")
        ecomerrce4 = request.POST.get("ecomerrce4")
        ecomerrce5 = request.POST.get("ecomerrce5")
        ecomerrce6 = request.POST.get("ecomerrce6")
        ecomerrce7 = request.POST.get("ecomerrce7")
        ecomerrce8 = request.POST.get("ecomerrce8")
        ecomerrce9 = request.POST.get("ecomerrce9")
        ecomerrce10 = request.POST.get("ecomerrce10")
        ecomerrce11 = request.POST.get("ecomerrce11")
        ecomerrce12 = request.POST.get("ecomerrce12")
        ecomerrce13 = request.POST.get("ecomerrce13")
        ecomerrce14 = request.POST.get("ecomerrce14")
        ecomerrce15 = request.POST.get("ecomerrce15")
        ecomerrce16 = request.POST.get("ecomerrce16")
        ecomerrce17 = request.POST.get("ecomerrce17")
        ecomerrce18 = request.POST.get("ecomerrce18")
        ecomerrce19 = request.POST.get("ecomerrce19")
        ecomerrce20 = request.POST.get("ecomerrce20")
        #Short answer
        ecomerrce21 = request.POST.get("ecomerrce21")
        ecomerrce22 = request.POST.get("ecomerrce22")
        ecomerrce23 = request.POST.get("ecomerrce23")
        ecomerrce24 = request.POST.get("ecomerrce24")
        ecomerrce25 = request.POST.get("ecomerrce25")
        ecomerrce26 = request.POST.get("ecomerrce26")
        ecomerrce27 = request.POST.get("ecomerrce27")
        ecomerrce28 = request.POST.get("ecomerrce28")
        ecomerrce29 = request.POST.get("ecomerrce29")
        ecomerrce30 = request.POST.get("ecomerrce30")
        # Medium answer
        ecomerrce40 = request.POST.get("ecomerrce40")
        ecomerrce41 = request.POST.get("ecomerrce41")
        #Long Answer
        ecomerrce50 = request.POST.get("ecomerrce50")
        True_false_result = [ ecomerrce000, ecomerrce001, ecomerrce002, ecomerrce003, ecomerrce004,  ecomerrce005,  ecomerrce006,
                               ecomerrce007,  ecomerrce008,  ecomerrce009]

        Multiple_choice_result = [ecomerrce1,ecomerrce2, ecomerrce3, ecomerrce4, ecomerrce5, ecomerrce6, ecomerrce7, ecomerrce8,
                                  ecomerrce9, ecomerrce10, ecomerrce11, ecomerrce12, ecomerrce13, ecomerrce14, ecomerrce15, ecomerrce16,
                                  ecomerrce17, ecomerrce18, ecomerrce19, ecomerrce20]
        Short_answer = [ecomerrce21,ecomerrce22,ecomerrce23,ecomerrce24,ecomerrce25,ecomerrce26,ecomerrce27,ecomerrce28,ecomerrce29,
                        ecomerrce30]
        Medium_answer = [ ecomerrce40, ecomerrce41]
        Long_answer = [ecomerrce50]

        print(True_false_result)
        print(Multiple_choice_result)
        print(Short_answer)
        print(Medium_answer)
        print(Long_answer)
        r = Exam_result(Student_ID  = hold_user, True_false_result = True_false_result,Multiple_choice_result = Multiple_choice_result,
                        Short_answer = Short_answer, Medium_answer  = Medium_answer, Long_answer = Long_answer)
        r.save()
    return render(request,'Home.html')