from django.contrib import admin
from django.urls import path
from .views import  home_aluno
 

urlpatterns = [

    path('aluno_home/',  home_aluno, name = 'sweet_home'),
    


]
