from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from members.serializers import AuthorSerializer , MemberSerializer
from members.models import Author , Member
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GetAllMember(APIView):
    def get(self,request):
        members = Member.objects.all()
        serializer = MemberSerializer(members , many=True)
        return Response(serializer.data)


    
    
