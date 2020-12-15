from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import Post

# Create your views here.

# splash page
def splash_view(request):
    return render(request, 'splash.html', {})

# main page
def main_view(request):
    if not request.user.is_authenticated:
        return redirect('/splash')    

    # creating a post
    if request.method == 'POST':
        post = Post.objects.create(
            title=request.POST['title'],
            body=request.POST['body'],
            author=request.user,
            created_at=datetime.now()
        )

    # render posts page
    posts = Post.objects.all().order_by('-created_at')
    # posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'main.html', {'posts': posts})

# viewing another user page
def user_view(request, username):
    user = User.objects.get(username=username)
    # chirps = Chirp.objects.filter(author=user).order_by('-created_at')
    return render(request, 'user.html', { 'user': user })



# deleting a post
def delete_view(request):
    # post = Post.objects.get(id=request.POST???, request???)
    post = Post.objects.get(id=request.GET['id'])
    if post.author == request.user:
        post.delete()
    return redirect('/')

# login, logout, signup
def login_view(request):
    username, password = request.POST['username'], request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/splash?error=LoginError')

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
    return redirect('/splash')