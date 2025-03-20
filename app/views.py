from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from app.models import Article


class ArticleListView(ListView):
    template_name = "app/home.html"
    model = Article
    context_object_name = "articles"


class ArticleCreateView(CreateView):
    template_name = "app/article_create.html"
    model = Article
    fields = ["title", "status", "content", "word_count", "twitter_post"]
    success_url = reverse_lazy("app.home")


class ArticleUpdateView(UpdateView):
    template_name = "app/article_update.html"
    model = Article
    fields = ["title", "status", "content", "word_count", "twitter_post"]
    success_url = reverse_lazy("app.home")
    context_object_name = "article"


class ArticleDeleteView(DeleteView):
    template_name = "app/article_delete.html"
    model = Article
    success_url = reverse_lazy("app.home")
    context_object_name = "article"


class ArticleDetailView(DetailView):
    template_name = "app/article_detail.html"
    model = Article
    context_object_name = "article"
    success_url = reverse_lazy("app.home")


# def create_article(request):
#     if request.method == "POST":
#         # data is submitted
#         form = CreateArticleForm(request.POST)
#         if form.is_valid():
#             fcd = form.cleaned_data()
#             new_article = Article(
#                 title=fcd["title"],
#                 status=fcd["status"],
#                 content=fcd["content"],
#                 word_count=fcd["word_count"],
#                 twitter_post=fcd["twitter_post"],
#             )
#             new_article.save()

#             return redirect("app.home")

#     else:
#         form = CreateArticleForm()

#     return render(request, "app/article_create.html", {"form": form})
