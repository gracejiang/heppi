from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime

from main.models import Post

# Create your views here.

# main page
def main_view(request):
    # decide between POST & GET request

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