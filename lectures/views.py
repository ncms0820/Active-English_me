from lectures.models import Lecture
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LectureSerializer
# Create your views here.


class LectureList(APIView):
    def get(self, request, format=None):
        Lectures = Lecture.objects.all()
        serializer = LectureSerializer(Lectures, many=True)
        return Response(serializer.data)
