from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('cadastro/', views.SignUpView.as_view(), name='cadastro'),
    path('login/', views.Login.as_view()),
]