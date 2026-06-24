from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from members.serializers import AuthorSerializer
from members.models import Author
# Create your views here.

class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer