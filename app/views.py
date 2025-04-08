from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from app.models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "app/home.html"
    model = Article
    context_object_name = "articles"
    paginate_by = 3

    def get_queryset(self):
        """Get Article only by the creator"""
        queryset = super().get_queryset().filter(creator=self.request.user)
        return queryset.order_by("-created_at")


class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "app/article_create.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("app.home")
    success_message = "Article created successfully"

    def form_valid(self, form):
        """Set/Insert creator during form_valid"""
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "app/article_update.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("app.home")
    context_object_name = "article"

    def test_func(self):
        """Add condition to only the creator who can update the article"""
        return self.request.user == self.get_object().creator


class ArticleDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    template_name = "app/article_delete.html"
    model = Article
    success_url = reverse_lazy("app.home")
    context_object_name = "article"

    def post(self, request, *args, **kwargs):
        messages.success(
            request, "Article deleted successfully", extra_tags="destructive"
        )
        return super().post(request, *args, **kwargs)

    def test_func(self):
        return self.request.user == self.get_object().creator


class ArticleDetailView(LoginRequiredMixin, DetailView):
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
