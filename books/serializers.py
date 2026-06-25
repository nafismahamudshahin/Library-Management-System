from rest_framework import serializers
from books.models import Book ,Category , Review
from members.serializers import AuthorSerializer

# Category serializer:
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description']

# Book serializer:
class RootLabelBookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = ['id','title','isbn','author','category','published_year','stock','created_at']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','isbn','category','published_year','stock','created_at']

    def create(self, validated_data):
        author_id = self.context['author_id']
        return Book.objects.create(author_id=author_id , **validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','books','member','review_context','review_context',]