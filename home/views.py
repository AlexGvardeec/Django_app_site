from django.http import HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from home.models import Article


# Создаем контроллер для списка статей в меню Блог
def article_list(request: HttpRequest):
    articles = Article.objects.all()
    return render(
        request,
        'home/article/list.html',
        {
            'articles': articles,
        }
    )


# Создаем контроллер для отображения статьи
def article_detail(request: HttpRequest, slug: str):
    article = get_object_or_404(Article, slug=slug)
    return render(
        request,
        'home/article/detail.html',
        {
            'article': article,
        }
    )
