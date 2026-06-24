from rest_framework import serializers
from members.models import Author

# Author serializer:
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','biography','nationality','birth_date','created_at']
