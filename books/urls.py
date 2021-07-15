from django.urls import path
from .views import BookList, BookDetail, AddBook

urlpatterns = [
    path('', BookList.as_view()),
    path('<int:pk>/', BookDetail.as_view()),
    path('add/', AddBook.as_view()),
]
