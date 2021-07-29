from django.urls import path
from .views import LectureList, ActiveLectureList, LectureDetail, AddLecture

urlpatterns = [
    path('', LectureList.as_view()),
    path('add/', AddLecture.as_view()),
    path('<int:pk>/', LectureDetail.as_view()),
    path('active/', ActiveLectureList.as_view()),
]
