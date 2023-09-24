from django.shortcuts import render, redirect
from .models import Post, Category, Comments
from django.http import HttpResponse
from newsapi import NewsApiClient


# Create your views here.


def create_post(request):
    categories = Category.objects.all()
    
    newsapi = NewsApiClient(api_key ='b4c6be38afa44bb3aac18e7a80270e23')
    top = newsapi.get_top_headlines(sources ='techcrunch')

    l = top['articles']
    dsc =[]
    nws =[]
    im =[]

    for i in range(len(l)):
      f = l[i]
      nws.append(f['title'])
      dsc.append(f['description'])
      im.append(f['urlToImage'])
      mylist = zip(nws, dsc, im)
    
    
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
            "mylist":mylist,
        }
        
        return render(request, 'blog/create_post.html', context)


def lenta(request):
    posts = Post.objects.all()
    
    if request.method == "POST":
        pass
    
    newsapi = NewsApiClient(api_key ='b4c6be38afa44bb3aac18e7a80270e23')
    top = newsapi.get_top_headlines(sources ='techcrunch')

    l = top['articles']
    dsc =[]
    nws =[]
    im =[]

    for i in range(len(l)):
      f = l[i]
      nws.append(f['title'])
      dsc.append(f['description'])
      im.append(f['urlToImage'])
      mylist = zip(nws, dsc, im)
    
    context = {
        'posts': posts,
        'title': 'Blog',
        "mylist":mylist,
    }
    
    return render(request, 'blog/blog_lenta.html', context)
