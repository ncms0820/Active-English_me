from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from books.models import Book
# Create your views here.


class BookList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


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
