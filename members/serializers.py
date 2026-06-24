from rest_framework import serializers
from members.models import Author , Member

# Author serializer:
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','biography','nationality','birth_date','created_at']

# member serializer
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['first_name','last_name','email','phone','address']