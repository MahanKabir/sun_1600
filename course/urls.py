
from django.urls import path
from . import views
urlpatterns = [
    path('create', views.create, name = "course.create"),
    path('read', views.read, name = "course.view"),
    path('delete/<int:id>', views.delete, name = "course.delete"),
    path('update/<int:id>', views.update, name = "course.update"),
]