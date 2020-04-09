from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    # posts = Post.objects.all().order_by('-id')
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)
