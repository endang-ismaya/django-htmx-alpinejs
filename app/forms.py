from django import forms
from app.models import ARTICLE_STATUS


class CreateArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    status = forms.ChoiceField(choices=ARTICLE_STATUS)
    content = forms.CharField(widget=forms.Textarea)
    word_count = forms.IntegerField()
    twitter_post = forms.CharField(widget=forms.Textarea, required=False)
