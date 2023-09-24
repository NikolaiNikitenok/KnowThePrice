from django.shortcuts import render
from newsapi import NewsApiClient

# Создание функции представления
def news_main(request):

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

    return render(request, 'news/news_main.html', context ={"mylist":mylist})
