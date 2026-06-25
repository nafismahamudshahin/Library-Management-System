from rest_framework import serializers
from borrows.models import BorrowRecord

    # book = models.ForeignKey(Book, on_delete=models.PROTECT , related_name="borrow_records")
    # member = models.ForeignKey(Member, on_delete=models.CASCADE , related_name="borrowings")
    # borrow_date = models.DateField(auto_now_add=True)
    # due_date = models.DateField()
    # return_date = models.DateField(null=True,blank=True)
    # is_returned = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)

# borrow serializer:
class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['id','book','member','due_date','is_returned']