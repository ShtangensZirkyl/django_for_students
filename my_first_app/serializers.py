from rest_framework import serializers

from my_first_app.models import Book


class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = '__all__'
