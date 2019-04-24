from django.shortcuts import render, redirect
# from .models import User, Post
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
    pass

def edit_user(request):
    pass

def show_user(request):
    pass

def post(request):
    pass