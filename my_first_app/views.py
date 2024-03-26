from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from my_first_app.models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def hello(request):
    books = BookSerializer(Book.objects.all(), many=True)
    return Response(books.data)
