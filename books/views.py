from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from books.models import Book , Category
from books.serializers import BookSerializer , CategorySerializer , RootLabelBookSerializer
# Create your views here.
# category viewset:
class CagegoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# book viewset
class RootLabelBookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = RootLabelBookSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(author_id=self.kwargs['author_pk'])

    def get_serializer_context(self):
        return {'author_id':self.kwargs['author_pk']}


