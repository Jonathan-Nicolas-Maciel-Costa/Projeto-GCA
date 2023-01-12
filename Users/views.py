from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView

from . import forms
import datetime



class SignUpView(CreateView):
    form_class = forms.CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/cadastro.html'
    model = CustomUser

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response



class Login(LoginView):



    form_class = forms.Login
    success_url = reverse_lazy('login')
    template_name = 'registration/login.html'
    model = CustomUser


    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_atual = datetime.date.today()
        context = {
                    'dia_hoje' : data_atual.day,
                    'form' : forms.Login
        }
        return context
