from django.shortcuts import render, get_object_or_404
from .models import Article

def blog_list(request):
    articles = Article.objects.filter(published=True)
    return render(request, 'blog/list.html', {'articles': articles})

def blog_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, published=True)
    return render(request, 'blog/detail.html', {'article': article})
