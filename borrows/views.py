from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from borrows.models import BorrowRecord
from borrows.serializers import BorrowRecordSerializer
# Create your views here.


class BorrowModelViewSet(ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer