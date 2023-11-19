from django.urls import path
from . import views

urlpatterns = [
    path("students", views.get_students, name="students"),
    path("add_student", views.create_student, name="add_student"),
    path("delete_student", views.delete_student, name="delete_student")
]
