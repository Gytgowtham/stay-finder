from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_page(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        if user:
            login(request, user)
            return redirect("/home/")
    return render(request, "accounts/login.html")


def signup_page(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        return redirect("/")
    return render(request, "accounts/signup.html")


def home(request):
    return render(request, "accounts/home.html")


# 🔥 ONLY THIS PAGE WE CARE NOW
def select_area(request):
    return render(request, "accounts/select_area.html")


def logout_page(request):
    logout(request)
    return redirect("/")
