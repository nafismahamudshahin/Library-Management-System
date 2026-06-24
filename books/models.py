from django.db import models
from members.models import Author
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author , on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name="books")
    published_year = models.DateField(blank=True , null=True)
    stock = models.PositiveIntegerField(blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

