from users.models import User
from rest_framework import serializers
from .models import Post, Comment


class UserField(serializers.RelatedField):
    def to_representation(self, value):
        data = {
            'username': value.username,
            'teacher': value.teacher,
        }
        return data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'pk',
            'contents',
            'user',
            'post'
        ]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = [
            'pk',
            'contents',
            'user',
            'comments',
            'likes',
        ]
