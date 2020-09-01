from django.shortcuts import render
from article.forms import ArticleForm
from blog.models import Blog
from article.models import Article
# Create your views here.

def create(request, id):
    blog = Blog.objects.get(id = id)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.blog_id = id
            f.save()

    else:
        form = ArticleForm()

    return render(request, 'admin/article/create.html', {'form': form, 'blog': blog})


def read(request, id):
    articles = Article.objects.all()
    blog = Blog.objects.get(id = id)
    return render(request, 'admin/article/view.html', {'articles': articles, 'blog': blog})