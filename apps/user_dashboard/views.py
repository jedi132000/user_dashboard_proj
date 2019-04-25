from django.shortcuts import render, redirect
from .models import User, Post
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'user_dashboard/index.html')


def register(request):
    return render(request, 'user_dashboard/register.html')

def create(request):
    errors = User.objects.easy_register_validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect('/register/')
    this_user = User.objects.easy_user_create(request.POST)
    print('-'*50)
    print(this_user)
    print('-'*50)
    return redirect('/signin')

def signin(request):
    return render(request, 'user_dashboard/signin.html')

def login(request):
    errors = User.objects.easy_login_validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect('/signin/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    if user.user_level == 9:
        return redirect('/dashboard/admin/')
    else:
        return redirect('/dashboard/')


def dashboard(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, 'user_dashboard/dashboard.html', context)

def admin_dashboard(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, 'user_dashboard/admin-dashboard.html', context)

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