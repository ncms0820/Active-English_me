from django.core.exceptions import AppRegistryNotReady
from lectures.models import ActiveLecture, Lecture
from users.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LectureSerializer, ActiveLectureSerializer
# Create your views here.


class LectureList(APIView):
    def get(self, request, format=None):
        lectures = Lecture.objects.all()
        serializer = LectureSerializer(lectures, many=True)
        return Response(serializer.data)

class LectureDetail(APIView):
    def get_object(self, pk):
        try:
            return Lecture.objects.get(pk=pk)
        except Lecture.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        lecture = self.get_object(pk)
        serializer = LectureSerializer(lecture)
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        lecture = self.get_object(pk)
        data = request.data
        serializer = LectureSerializer(lecture, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        lecture = self.get_object(pk)
        lecture.delete()
        return Response(status=status.HTTP_200_OK)

class AddLecture(APIView):
    def post(self, request, format=None):
        data = request.data
        serializer = LectureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ActiveLectureList(APIView):
    def post(self, request, format=None):
        data = request.data
        user = User.objects.get(pk=data['user'])
        active_lectures = ActiveLecture.objects.filter(user=user)
        serializer = ActiveLectureSerializer(active_lectures, many=True)
        return Response(serializer.data)



