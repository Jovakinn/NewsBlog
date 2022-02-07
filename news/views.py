from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render

from news.models import News, Category


def index(request: Request) -> HttpResponse:
    news = News.objects.all()
    categories = Category.objects.all()
    context: dict = {
        'news': news,
        'title': 'Список новин',
        'categories': categories,
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request: Request, category_id: int):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context: dict = {
        'news': news,
        'categories': categories,
        'category': category,
    }
    return render(request, template_name='news/category.html', context=context)
