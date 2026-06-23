from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser , AbstractUser
from members.managers import CustomUserManager
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(null=True,blank=True)
    nationality = models.CharField(max_length=100)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Member(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13 , blank=True)
    address = models.TextField(max_length=255 , blank=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]
