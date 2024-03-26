from django.contrib import admin

# Register your models here.
from my_first_app.models import Book

admin.site.register(Book)
