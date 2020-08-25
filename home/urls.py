from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register2/', views.register2, name='register2'),
    path('', views.login, name='login'),


]
