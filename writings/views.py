from writings.models import Writing
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WritingSerializer
# Create your views here.


class WritingList(APIView):
    def get(self, request, format=None):
        Writings = Writing.objects.all()
        serializer = WritingSerializer(Writings, many=True)
        return Response(serializer.data)
