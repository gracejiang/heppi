from django.shortcuts import render
from main.models import Posts

# Create your views here.

def main_view(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts})