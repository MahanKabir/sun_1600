

from django.urls import path
from . import views
urlpatterns = [
    path('create', views.create, name = 'article.create'),
    # path('read', views.read, name = 'article.read'),
    # path('update', views.update, name = 'article.update'),
    # path('delete', views.delete, name = 'article.delete'),
]