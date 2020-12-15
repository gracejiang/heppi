from django.shortcuts import render, redirect, get_object_or_404
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

    return render(request, 'main.html' )

# discover page
def discover_view(request):
    # render posts page
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'discover.html', {'posts': posts})


# creating a new post view
def new_post_view(request):
    # creating a post
    if request.method == 'POST':
        post = Post.objects.create(
            title=request.POST['title'],
            body=request.POST['body'],
            author=request.user,
            created_at=datetime.now()
        )
        return redirect('/user/' + request.user.username)    

    return render(request, 'new_post.html', {})


# viewing a post
def post_details_view(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_details.html', { 'post_details': post })
    

# viewing another user page
def user_view(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user).order_by('-created_at')
    return render(request, 'user.html', { 'user': user, 'all_posts': posts })

# edit profile
def edit_profile_view(request):
    user = request.user

    # edited profile
    if request.method == 'POST':
        user.profile.bio = request.POST['bio']
        user.save()
        posts = Post.objects.filter(author=user).order_by('-created_at')
        return redirect('/user/' + user.username)

    return render(request, 'edit_profile.html', { 'user': user })

# deleting a post
def delete_view(request, username):
    post = Post.objects.get(id=request.GET['id'])
    user = request.user
    if post.author == user:
        post.delete()
    return redirect('/user/' + user.username)

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
