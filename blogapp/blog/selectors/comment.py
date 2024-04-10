from blogapp.blog.models import Comment
from blogapp.blog.selectors.post import post_detail


def post_comment_list(*, post_id: int) -> Comment:
    """
    Retrieve a queryset of Comment instances associated with a specific Post instance.

    Args:
        post_id (int): The primary key (ID) of the Post instance to retrieve the comments for.

    Returns:
        Comment: A queryset of Comment instances associated with the specified Post instance.

    Raises:
        Exception: If there is an error retrieving the Post instance or the associated comments.
    """
    post_instance = post_detail(pk=post_id)
    qs = Comment.objects.filter(post=post_instance)
    return qs
