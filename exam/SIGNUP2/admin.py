from django.contrib import admin
from .models import My_Student1,one_time_access_check,Student_signup_record1, Exam_result
    # Student_signup_r,Student_signup_record_store,Student_signup,

# Register your models here.
admin.site.register(My_Student1)
# admin.site.register(man)
admin.site.register(Student_signup_record1)
# admin.site.register(Student_signup_r)
admin.site.register(one_time_access_check)
admin.site.register(Exam_result)
# admin.site.register(Student_signup_record_store)
