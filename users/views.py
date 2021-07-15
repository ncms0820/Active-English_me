from collections import UserString
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
# Create your views here.


class UserList(APIView):
    def get(self, request, format=None):
        Users = User.objects.all()
        serializer = UserSerializer(Users, many=True)
        return Response(serializer.data)
