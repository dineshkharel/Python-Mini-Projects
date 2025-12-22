from django.contrib import admin
from django.urls import path
from .views import register,loginEmpolyee,home,logout_user

urlpatterns = [
    path('',loginEmpolyee, name='login'),
    path("register/", register, name="register"),
    path("home/", home, name="home"),
    path("logout/", logout_user, name="logout"),

]
