from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    price = models.CharField(max_length=15)
    image = models.ImageField(upload_to='static/images/course/')