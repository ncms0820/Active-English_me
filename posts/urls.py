from django.urls import path
from .views import PostList, AddLikes

urlpatterns = [
    path('', PostList.as_view()),
    path('likes/<int:pk>', AddLikes.as_view()),
]
