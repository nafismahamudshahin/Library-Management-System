from rest_framework import serializers
from borrows.models import BorrowRecord
from members.serializers import GetMemberSerializer
from books.serializers import RootLabelBookSerializer

# borrow serializer:
class BorrowRecordSerializer(serializers.ModelSerializer):
    member = GetMemberSerializer()
    book = RootLabelBookSerializer()
    class Meta:
        model = BorrowRecord
        fields = ['id','book','member','due_date','is_returned']