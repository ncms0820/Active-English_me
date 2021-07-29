from django.urls import path
from .views import WritingList, AddWriting, WritingDetail

urlpatterns = [
    path('', WritingList.as_view()),
    path('add/', AddWriting.as_view()),
    path('<int:pk>/', WritingDetail.as_view()),
]
