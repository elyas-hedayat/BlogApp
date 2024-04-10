from django.urls import path

from .apis.comment import CommentCreateApi, CommentListApi
from .apis.post import PostCreateApi, PostDetailApi, PostListApi, PostUpdateApi

app_name = "blog"

urlpatterns = [
    path("", PostListApi.as_view(), name="post-list"),
    path("<int:post_id>/", PostDetailApi.as_view(), name="post-detail"),
    path("create/", PostCreateApi.as_view(), name="post-create"),
    path("<int:post_id>/update/", PostUpdateApi.as_view(), name="post-update"),
    path("comments/<int:post_id>/", CommentListApi.as_view(), name="comment-list"),
    path("comments/create/", CommentCreateApi.as_view(), name="comment-create"),
]
