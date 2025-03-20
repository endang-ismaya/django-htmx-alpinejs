from django.urls import path

from app import views

urlpatterns = [
    path("", views.home, name="app.home"),
    path("articles/create/", views.create_article, name="app.create_article"),
    path(
        "articles/createview/",
        views.ArticleCreateView.as_view(),
        name="app.create_article_view",
    ),
]
