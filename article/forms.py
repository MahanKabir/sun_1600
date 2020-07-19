
from django import forms
from docutils.nodes import field

from article.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'page', 'price', 'author', 'image']