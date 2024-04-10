from django.urls import include, path

urlpatterns = [
    path("blog/", include(("blogapp.blog.urls", "blog"))),
    path("auth/", include(("blogapp.authentication.urls", "auth"))),
]
