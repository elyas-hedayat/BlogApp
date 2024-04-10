from django.urls import path

from .apis.post import PostListApi, PostDetailApi, PostCreateApi, PostUpdateApi
from .apis.comment import CommentListApi, CommentCreateApi

app_name = "blog"

urlpatterns = [
    path("", PostListApi.as_view(), name="post-list"),
    path("<int:post_id>/", PostDetailApi.as_view(), name="post-detail"),
    path("create/", PostCreateApi.as_view(), name="post-create"),
    path("<int:post_id>/update/", PostUpdateApi.as_view(), name="post-update"),
    path("comments/<int:post_id>/", CommentListApi.as_view(), name="comment-list"),
    path("comments/create/", CommentCreateApi.as_view(), name="comment-create")
]
