from django.urls import path
from .views import WritingList

urlpatterns = [
    path('', WritingList.as_view()),
]
