from django.shortcuts import render
from article.forms import ArticleForm

# Create your views here.

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = ArticleForm()

    return render(request, 'admin/article/create.html', {'form': form})