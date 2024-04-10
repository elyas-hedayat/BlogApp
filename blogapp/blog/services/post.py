from rest_framework.generics import get_object_or_404

from blogapp.blog.models import Post
from blogapp.common.services import model_update


def post_create(*, title: str, content: str) -> Post:
    """
    Create a new Post instance.

    Args:
        title (str): The title of the new post.
        content (str): The content of the new post.

    Returns:
        Post: The newly created Post instance.
    """
    post = Post.objects.create(
        title=title,
        content=content,
    )
    return post


def post_update(pk: int, data: dict) -> Post:
    """
    Update an existing Post instance.

    Args:
        pk (int): The primary key (ID) of the Post instance to be updated.
        data (dict): A dictionary containing the fields to be updated and their new values.

    Returns:
        Post: The updated Post instance.

    Raises:
        Http404: If the Post instance with the given primary key does not exist.
    """
    instance = get_object_or_404(Post, pk=pk)
    fields = list(data.keys())
    post, updated = model_update(instance=instance, fields=fields, data=data)
    return post
