from django.db import models

# Create your models here.
from blog.models import Blog

class Article(models.Model):
    name = models.CharField(max_length=45)
    page = models.CharField(max_length=4)
    price = models.CharField(max_length=20)
    author = models.CharField(max_length=45)
    image = models.ImageField(upload_to='static/images/artice/')
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)