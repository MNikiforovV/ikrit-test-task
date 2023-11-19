from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Student, Course

def get_students(request):
    students = Student.objects.all().values()
    output = [entry for entry in students]
    return JsonResponse(output, safe=False)


def create_student(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        surname = data.get("surname")
        course_id = data.get("course")

        #course = Course.objects.get(id=course_id)

        student = Student.objects.create(
            name=name,
            surname=surname,
            course_id=course_id
        )

        student.save()
        return HttpResponse(status=200)


def delete_student(request):
    if request.method == "POST":
        data = request.POST
        student_id = data.get("student_id")
        student = Student.objects.get(id=student_id)
        student.delete()
        student.save()
        return HttpResponse(status=200)
