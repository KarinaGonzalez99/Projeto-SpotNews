from django.shortcuts import render
from .models import News


def home(request):
    news_list = News.objects.all()
    return render(request, 'home.html', {'news_list': news_list})
