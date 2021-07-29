from django.urls import path
from .views import PostList, AddLikes, PostDetail, AddPost, AddComment, CommentDetail

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('<int:pk>/likes/', AddLikes.as_view()),
    path('add/', AddPost.as_view()),
    path('comments/add/', AddComment.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
]
