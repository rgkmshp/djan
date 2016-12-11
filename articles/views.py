from django.shortcuts import render
from articles.models import Article

# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    response = render(request, 'articles.html', context)
    return response