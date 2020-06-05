from django.shortcuts import render, HttpResponse, redirect
# from exam.LOGIN.models import Student_signup_record
# Create your views here.
# def login(request):
#      return render(request,"login.html")
# def exam(request):
#      if request.method == 'POST':
#           college_idl = request.POST['college_id']
#           password = request.POST['password']
#           from django.contrib import auth
#           x = auth.authenticate(college_id = college_idl,  password = password)
#           print(college_idl,password)
#           if x is None:
#                return render(request, 'login.html')
#           else:
#                return render(request, "exam.html")
