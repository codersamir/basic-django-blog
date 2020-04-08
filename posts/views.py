from django.shortcuts import render
from .models import Post


def home(request):
    # posts = Post.objects.all().order_by('-id')
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


def detail(request):
    return render(request, 'detail.html')
