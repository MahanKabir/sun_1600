
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name = "blog.create"), #localhost:8000/admin/blog/create
    path('read', views.read, name = "blog.read"), #localhost:8000/admin/blog/read
    path('update/<int:id>', views.update, name = "blog.update"),
    path('delete/<int:id>', views.delete, name = "blog.delete"),
]