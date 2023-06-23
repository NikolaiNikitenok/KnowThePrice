from django.shortcuts import render, redirect
from .models import Post, Category, Comments
from django.http import HttpResponse

# Create your views here.


def create_post(request):
    categories = Category.objects.all()
    
    
    if request.method == "POST":
        if "Create" in request.POST:
            title = request.POST['title']
            author = request.user
            description = request.POST['description']
            category = request.POST['category_select']
            tags = request.POST['tags']
            
            post = Post(title=title, description=description, author=author, category=Category.objects.get(name=category), tags=tags)
            post.save()
            
        return redirect('blog-lenta')    
        
    else:
            
        context = {
            'categories': categories,
            'title': 'Create Post',
        }
        
        return render(request, 'blog/create_post.html', context)


def lenta(request):
    posts = Post.objects.all()
    
    if request.method == "POST":
        pass
    
    context = {
        'posts': posts,
        'title': 'Blog'
    }
    
    return render(request, 'blog/blog_lenta.html', context)
