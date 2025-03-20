from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from app.forms import CreateArticleForm
from app.models import Article


def home(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "app/home.html", context)


class ArticleCreateView(CreateView):
    template_name = "app/article_create.html"
    model = Article
    fields = ["title", "status", "content", "word_count", "twitter_post"]
    success_url = reverse_lazy("app.home")


def create_article(request):
    if request.method == "POST":
        # data is submitted
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            fcd = form.cleaned_data()
            new_article = Article(
                title=fcd["title"],
                status=fcd["status"],
                content=fcd["content"],
                word_count=fcd["word_count"],
                twitter_post=fcd["twitter_post"],
            )
            new_article.save()

            return redirect("app.home")

    else:
        form = CreateArticleForm()

    return render(request, "app/article_create.html", {"form": form})
