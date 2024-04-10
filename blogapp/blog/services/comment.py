from blogapp.blog.models import Comment


def comment_create(*, post: int, email: str, text: str, parent: None | int) -> Comment:
    comment = Comment.objects.create(
        post_id=post,
        email=email,
        text=text,
        parent_id=parent,
    )
    return comment
