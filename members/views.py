from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from members.serializers import AuthorSerializer , GetMemberSerializer , AddMemberSerializer
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
        serializer = GetMemberSerializer(members , many=True)
        return Response(serializer.data)


class MemberModelViewSet(ModelViewSet):
    queryset = Member.objects.all()
    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddMemberSerializer
        else:
            return GetMemberSerializer
    
