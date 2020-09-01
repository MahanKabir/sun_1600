

from django.urls import path
from . import views
urlpatterns = [
    path('create/<int:id>', views.create, name = 'article.create'), #localhost:8000/admin/article/create
    path('read/<int:id>', views.read, name = 'article.read'),
    # path('update', views.update, name = 'article.update'),
    # path('delete', views.delete, name = 'article.delete'),
]