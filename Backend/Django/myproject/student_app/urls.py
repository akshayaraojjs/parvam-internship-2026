from django.urls import path
from .import views

urlpatterns = [
    path('', views.student_list, name="list_of_students"),
    path('form/', views.student_form, name="registration_form"),
    path('info/', views.student_info, name="student_details"),
]