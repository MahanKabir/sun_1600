
from django.urls import path
from . import views
urlpatterns = [
    path('create', views.create, name = "course.create"),
    path('read', views.read)
]