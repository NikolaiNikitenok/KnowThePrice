from django.shortcuts import render
from .models import Post, Category, Comments
from django.http import HttpResponse

# Create your views here.

def lenta(request):
    posts = Post.objects.all()
    
    context = {
        'posts': posts,
        'title': 'Blog'
    }
    
    return render(request, 'blog/blog_lenta.html', context)
