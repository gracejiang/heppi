from django.shortcuts import render
from main.models import Post

# Create your views here.

# main page
def main_view(request):
    # decide between POST & GET request

    # if POST, insert into DB
    if request.method == 'POST':
        post = Post.objects.create(
            title=request.POST['title'],
            body=request.POST['body'],
        )

    # if GET, render page
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts})