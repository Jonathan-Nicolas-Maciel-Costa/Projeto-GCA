from django.contrib import admin
from django.urls import path
from .views import  home_view,\
                    sign_up_student_view,\
                    sign_up_teacher_view,\
                    sign_up_course_view,\
                    sign_up_subject_view,\
                    register_coordinator_view,\
                    teste_view,\
                    SignUpView_Student,\
                    SignUpView_Teacher

urlpatterns = [

    path('',  home_view, name = 'home'),

    path('adm/sigh_up_student/cadastro_Estudante/', SignUpView_Student.as_view(), name='cadastro_estudante'),
    path('adm/sigh_up_student/cadastro_Professor/', SignUpView_Teacher.as_view(), name='cadastro_professor'),

    path('adm/sigh_up_student',  sign_up_student_view, name = 'sign_up_student'),
    path('adm/sigh_up_teacher',  sign_up_teacher_view, name = 'sign_up_teacher'),
    path('adm/sigh_up_course',  sign_up_course_view, name = 'sign_up_course'),
    path('adm/sigh_up_subject',  sign_up_subject_view, name = 'sign_up_subject'),
    path('adm/register_coordinator',  register_coordinator_view, name = 'register_coordinator'),
    path('adm/teste',  teste_view, name = 'teste'),
]
