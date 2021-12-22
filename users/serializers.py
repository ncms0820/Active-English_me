from rest_framework import serializers
from .models import User

#dsdf
class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = [
            "gender",
            "bio",
            "birthday",
            "teacher",
        ]
