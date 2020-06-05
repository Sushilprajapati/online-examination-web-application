from django.shortcuts import render, HttpResponse, redirect

# def exam(request):
#     return render(request, "exam.html");
    # if request.method == 'POST':
    #     signup_College_Id = request.POST['signup_College_Id']
    #     signup_college_name = request.POST['signup_college_name']
    #     semester = request.POST['semester']
    #     signup_email = request.POST['signup_email']
    #     signup_password = request.POST['signup_password']       #
    #     #t =  Student_signup_record()
    #     x =  Student_signup_record( s_name = signup_college_name, password = signup_password, email =  signup_email,semester =semester, college_id = signup_College_Id )
    #     # x = User.objects.create_user.semester = semester
    #     # x = User.objects.create_user.college_id = signup_College_Id
    #     x.save()

    # else:
    #    return redirect('/')
