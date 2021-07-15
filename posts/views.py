from django.http.response import Http404
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from posts.models import Post
from users.models import User
# Create your views here.


class PostList(APIView):
    def get(self, request, format=None):
        Posts = Post.objects.all()
        serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data)


class AddLikes(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        id = request.data['pk']
        user = User.objects.get(pk=id)
        post = self.get_object(pk)
        # if
        post.likes.add(user)
        serializer = PostSerializer(post)
        return Response(serializer.data)


"""
class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        data = request.data
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_200_OK)


class AddBook(APIView):
    def post(self, request, format=None):
        data = request.data
        Serializer = BookSerializer(data=data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
"""
