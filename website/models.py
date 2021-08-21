from unicodedata import category
from django.db import models

# Create your models here.
class Products(models.Model):

    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="pics")
    description = models.TextField()
