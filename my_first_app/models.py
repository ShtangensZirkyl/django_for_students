from django.db import models

# Create your models here.


class Book(models.Model):
    author = models.TextField(blank=True)
    name = models.TextField(unique=True)
