from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html',  {'posts': posts})

def homework(request):
    return render(request, 'blog/homework.html')

def register(request):
    return render(request, 'blog/register.html')

def merch(request):
    return render(request, 'blog/merch.html')

def news(request):
    posts = Post.objects.all()

    return render(request, 'blog/news.html',  {'posts': posts})

def gallery(request):
    return render(request, 'blog/gallery.html')


# Create your views here.
