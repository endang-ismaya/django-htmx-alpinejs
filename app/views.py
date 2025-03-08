from django.shortcuts import render

from app.models import Article


def home(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "app/home.html", context)
