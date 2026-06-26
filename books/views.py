from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from books.models import Book , Category , Review
from books.serializers import BookSerializer , CategorySerializer , RootLabelBookSerializer , ReviewSerializer
from rest_framework.filters import SearchFilter
# Create your views here.

# category viewset:
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# book viewset
class RootLabelBookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = RootLabelBookSerializer
    filter_backends =[SearchFilter]
    search_fields = ['title','author__name','isbn','category__name']


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends =[SearchFilter]
    search_fields = ['title','author__name','isbn','category__name']

    def get_queryset(self):
        return Book.objects.filter(author_id=self.kwargs['author_pk'])

    def get_serializer_context(self):
        return {'author_id':self.kwargs['author_pk']}


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer