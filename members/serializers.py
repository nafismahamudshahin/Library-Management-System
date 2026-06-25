from rest_framework import serializers
from members.models import Author , Member

# Author serializer:
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','biography','nationality','birth_date','created_at']

# member serializer

class GetMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id','username','first_name','last_name','email','phone','address']

class AddMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['username','first_name','last_name','email','password','phone','address']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        return Member.objects.create_user(password=password,**validated_data)