from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(CourseSemester)
admin.site.register(StudentPersonalCard)
