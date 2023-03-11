from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import RegisterFrom
from .forms import PostForm

# Create your views here.

def home(req):
    posts = Post.objects.all()

    if req.method == "POST":
        post_id = req.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == req.user:
            post.delete()
    return render(req, "main/home.html", {"posts": posts})

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

@login_required(login_url="/login")
def create_post(req):
    if req.method == "POST":
        form = PostForm(req.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = req.user
            post.save()
            return redirect("/home")
    else:
            form = PostForm()
    return render(req, "main/create_post.html", {"form": form})

