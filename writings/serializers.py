from rest_framework import serializers
from .models import Writing


class WritingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writing
        fields = [
            "user",
            "title",
            "content",
            "likes",
        ]
