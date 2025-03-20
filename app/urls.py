from django.urls import path

from app import views

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="app.home"),
    # path("articles/create/", views.create_article, name="app.create_article"),
    path(
        "create/",
        views.ArticleCreateView.as_view(),
        name="app.create_article",
    ),
    path(
        "<int:pk>/update/",
        views.ArticleUpdateView.as_view(),
        name="app.update_article",
    ),
    path(
        "<int:pk>/delete/",
        views.ArticleDeleteView.as_view(),
        name="app.delete_article",
    ),
    path(
        "<int:pk>/detail/",
        views.ArticleDetailView.as_view(),
        name="app.detail_article",
    ),
]
