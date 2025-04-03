import re

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from app.managers import UserProfileManager

ARTICLE_STATUS = (
    ("draft", "draft"),
    ("inprogress", "in progress"),
    ("published", "published"),
)


class UserProfile(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    email = models.EmailField(max_length=255, unique=True)
    objects = UserProfileManager()


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default="")
    word_count = models.IntegerField(default=0)
    twitter_post = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=20,
        choices=ARTICLE_STATUS,
        default="draft",
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="articles",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        text = re.sub(r"<[^>]*>", "", self.content).replace("&nbsp;", " ")
        self.word_count = len(re.findall(r"\b\w+\b", text))
        return super().save(*args, **kwargs)
