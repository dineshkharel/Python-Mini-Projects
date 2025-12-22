from django.shortcuts import render,redirect
from .models import Employee
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method=="POST":
        full_name= request.POST.get("full_name")
        email= request.POST.get("email")
        password= request.POST.get("password")
        if Employee.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect("register")
    

        Employee.objects.create_user(
            email=email,
            password=password,
            full_name=full_name
        )
        messages.success(request,"Regestration Successful. You can now login ")
        return redirect("login")
    return render(request,"accounts/register.html")

def loginEmpolyee(request):
    if request.method =="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "accounts/login.html", {
                "error": "Invalid email or password"
            })

    return render(request, "accounts/login.html")

@login_required
def home(request):
    return render(request, "accounts/home.html", {"user": request.user})

def logout_user(request):
    logout(request)
    return redirect('login') 