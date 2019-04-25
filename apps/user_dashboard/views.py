from django.shortcuts import render, redirect
from .models import User, Post, Comment
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
    if 'user_id' not in request.session:
         return redirect('/signin')
    return redirect('/dashboard/')
   

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
    user = User.objects.get(id=request.session['user_id'])
    if user.user_level == 9:
        return redirect('/dashboard/admin/')
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

def edit_user(request,user_id):
    return render(request, 'user_dashboard/admin_edit.html')

def update_user(request):
    pass

def update_pw(request):
    pass

def update_desc(request):
    pass

def show_user(request, user_id):
    context = {
        "this_user" : User.objects.get(id=user_id),
        "other_users": User.objects.all().exclude(id=request.session['user_id']),
        "this_users_posts": Post.objects.filter(post_reciever=User.objects.get(id=user_id)),
        "all_comments": Comment.objects.all(),
    }
    return render(request,'user_dashboard/show.html', context)

def post(request, target_id):
    errors = Post.objects.validate_post(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect(f"/users/show/{target_id}")
    Post.objects.easy_post_create(request.POST, request.session['user_id'], target_id)

    return redirect (f"/users/show/{target_id}")
    
def comment(request, post_id, target_id):
    Comment.objects.easy_comment_create(request.POST, post_id, target_id)
    return redirect (f"/users/show/{target_id}")

def destroy(request):
    pass

def logout(request):
    request.session.clear()
    return redirect("/")