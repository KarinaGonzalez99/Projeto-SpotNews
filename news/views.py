from django.shortcuts import render
from .models import News


def home(request):
    news_list = News.objects.all()
    return render(request, 'home.html', {'news_list': news_list})


def news_details(request, id):
    news = News.objects.get(id=id)
    return render(request, 'news_details.html', {'news': news})
