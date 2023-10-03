from django import forms
from .models import Categories, News


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'author', 'created_at', 'image']
