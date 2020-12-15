from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import Post

# Create your views here.

# main page
def main_view(request):
    # if not request.user.is_authenticated:
    #     return redirect('/accounts')    

    # creating a post
    if request.method == 'POST':
        post = Post.objects.create(
            title=request.POST['title'],
            body=request.POST['body'],
            # posted_at=datetime.now()
        )

    # render posts page
    # posts = Post.objects.all().order_by('-posted_at')
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts})


# deleting a post
def delete_view(request):
    # post = Post.objects.get(id=request.POST???, request???)
    post = Post.objects.get(id=request.GET['id'])
    post.delete()
    return redirect('/')

# login/signup page
def accounts_view(request):
    return render(request, 'accounts.html', {})

def login_view(request):
    username, password = request.POST['username'], request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/accounts?error=LoginError')

def signup_view(request):
    # print(request.POST['username'], request.POST['password'], request.POST['email'], )
    user = User.objects.create_user(
        username=request.POST['username'],
        password=request.POST['password'],
        email=request.POST['email'],
    )

    login(request, user)
    return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/accounts')