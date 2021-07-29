from rest_framework.utils import field_mapping
from lectures.models import Lecture
from rest_framework import serializers
from .models import ActiveLecture, Lecture


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = [
            'pk',
            "title",
            "description",
            "start_time",
            "end_time",
            "teacher",
            "limit",
        ]


class ActiveLectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveLecture
        fields = [
            'pk',
            'status',
            'lecture',
            'user',
            "progress",
            "start_date",
            "end_date",
        ]
