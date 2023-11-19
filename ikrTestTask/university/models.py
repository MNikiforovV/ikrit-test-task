from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150, blank=False)
    number = models.IntegerField()

    def __str__(self) -> str:
        return f"Course {self.number} {self.title}"


class Student(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.name} {self.surname}, course {self.course}"


class StudentPersonalCard(models.Model):
    student_id = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Student card {self.name}"


class Semester(models.Model):
    number = models.IntegerField(blank=False)

    def __str__(self) -> str:
        return f"Semester {self.number}"


class Teacher(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    degree = models.CharField(max_length=60, blank=False)

    def __str__(self) -> str:
        return f"Teacher {self.name} {self.surname}, {self.degree}"


class CourseSemester(models.Model):
    course_id = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    semester_id = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE
    )
    date_start = models.DateField()
    date_end = models.DateField()

    teacher = models.ManyToManyField(Teacher)

    def __str__(self) -> str:
        return f"{self.semester_id} of {self.course_id}, starts at \
        {self.date_start}, ends at {self.date_end}"
