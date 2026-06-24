from rest_framework import serializers
from books.models import Book ,Category

# Category serializer:
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description']

# Book serializer:
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','author','isbn','category','publiched_year','stock','created_at']