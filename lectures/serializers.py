from rest_framework.utils import field_mapping
from lectures.models import Lecture
from rest_framework import serializers
from .models import ActiveLecture, Lecture


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = [
            "status",
            "title",
            "description",
            "start_time",
            "end_time",
            "teacher",
            "limit",
        ]


class AlectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveLecture
        fields = [
            "progress",
            "start_date",
            "end_date",
        ]
