from blogapp.blog.models import Comment


def comment_create(
    *, post: int, email: str, text: str, parent: None | int = None
) -> Comment:
    """
    Create a new comment associated with a specific post.

    Args:
        post (int): The primary key (ID) of the post to associate the comment with.
        email (str): The email address of the person who is posting the comment.
        text (str): The text content of the comment.
        parent (int, optional): The primary key (ID) of the parent comment, if this is a reply to an existing comment. Defaults to None.

    Returns:
        Comment: The newly created comment instance.

    Raises:
        Post.DoesNotExist: If the provided `post` ID does not exist.
        Comment.DoesNotExist: If the provided `parent` ID does not exist.
        Exception: If there is any other error creating the comment.
    """
    comment = Comment.objects.create(
        post_id=post,
        email=email,
        text=text,
        parent_id=parent,
    )
    return comment
