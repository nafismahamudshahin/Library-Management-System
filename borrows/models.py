from django.db import models
from books.models import Book
from members.models import Member
# Create your models here.
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT , related_name="borrow_records")
    member = models.ForeignKey(Member, on_delete=models.CASCADE , related_name="borrowings")
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True,blank=True)
    is_returned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.name} - {self.book.title}"