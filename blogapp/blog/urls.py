from django.urls import path

from .apis.post import PostListApi, PostDetailApi, PostCreateApi, PostUpdateApi

app_name = "blog"

urlpatterns = [
    path("", PostListApi.as_view(), name="list"),
    path("<int:post_id>/", PostDetailApi.as_view(), name="detail"),
    path("create/", PostCreateApi.as_view(), name="create"),
    path("<int:post_id>/update/", PostUpdateApi.as_view(), name="update"),
]
