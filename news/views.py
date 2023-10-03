from django.shortcuts import render, redirect
from .models import News, Categories
from .forms import CategoriesForm, NewsForm


def home(request):
    news_list = News.objects.all()
    return render(request, 'home.html', {'news_list': news_list})


def news_details(request, id):
    news = News.objects.get(id=id)
    return render(request, 'news_details.html', {'news': news})


def categories_form(request):
    if request.method == "POST":
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = CategoriesForm()
    return render(request, 'categories_form.html', {'form': form})


def news_form(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = NewsForm()

    categories = Categories.objects.all()

    return render(
        request, 'news_form.html', {'form': form, 'categories': categories}
        )
