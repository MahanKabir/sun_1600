from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:id>', views.create, name = "video.create"),
    path('read', views.read, name = "video.read"),

]