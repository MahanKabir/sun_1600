from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/images/blog/')
