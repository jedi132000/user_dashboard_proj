from django.shortcuts import render, redirect
from .models import User, Post
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'user_dashboard/index.html')


def register(request):
    return render(request, 'user_dashboard/register.html')

def create(request):
    return redirect('/signin')

def signin(request):
    return render(request, 'user_dashboard/signin.html')

def login(request):
    return redirect('/dashboard')

def dashboard(request):
    return render(request, 'user_dashboard/dashboard.html')

def admin_dashboard(request):
    return render(request, 'user_dashboard/admin-dashboard.html')

def new_user(request):
    return render(request, 'user_dashboard/new.html')

def edit(request):
    return render(request, 'user_dashboard/user_edit.html')

def edit_user(request):
    return render(request, 'user_dashboard/admin_edit.html')

def update_user(request):
    pass

def update_pw(request):
    pass

def update_desc(request):
    pass

def show_user(request):
    pass

def post(request):
    pass

def destroy(request):
    pass

def logout(request):
    request.session.clear()
    return redirect("/")