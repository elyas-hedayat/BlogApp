from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from blogapp.blog.filters import PostFilter
from blogapp.blog.models import Post


def post_detail(
    *,
    pk: int,
) -> Post:
    """
    Retrieve a single Post instance by its primary key.

    Args:
        pk (int): The primary key (ID) of the Post instance to retrieve.

    Returns:
        Post: The retrieved Post instance.

    Raises:
        Http404: If the Post instance with the given primary key does not exist.
    """
    return get_object_or_404(Post, pk=pk)


def post_list(
    *,
    filters=None,
) -> QuerySet[Post]:
    """
    Retrieve a queryset of Post instances, optionally filtered by a provided filters dictionary.

    Args:
        filters (dict, optional): A dictionary of filters to apply to the Post queryset. Defaults to None.

    Returns:
        QuerySet[Post]: The queryset of Post instances, potentially filtered.
    """
    filters = filters or {}
    qs = Post.objects.all()
    return PostFilter(filters, qs).qs
