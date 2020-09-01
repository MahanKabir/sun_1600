from django.shortcuts import render, redirect

# Create your views here.

from blog.forms import BlogForm
from blog.models import Blog


def create(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = BlogForm()
    return render(request, 'admin/blog/create.html', {'form': form})

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'admin/blog/view.html', {'blogs': blogs})

def update(request, id):
    blog = Blog.objects.get(id = id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
    else:
        form = BlogForm(instance=blog)
    return render(request, 'admin/blog/edit.html', {'form': form, 'blog': blog})

def delete(request, id):
    blog = Blog.objects.get(id = id)
    blog.delete()
    return render(request, 'admin/blog/view.html')