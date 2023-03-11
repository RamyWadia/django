from django.shortcuts import render, redirect
from .forms import RegisterFrom
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(req):
    return render(req, "main/home.html")

def sign_up(req):
    if req.method == "POST":
        form = RegisterFrom(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect("/home")
    else:
        form = RegisterFrom()
    return render(req, "registration/sign_up.html", {"form": form}) 