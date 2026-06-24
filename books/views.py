from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from books.models import Book , Category
from books.serializers import BookSerializer , CategorySerializer
# Create your views here.
# category viewset:
class CagegoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# book viewset
class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


