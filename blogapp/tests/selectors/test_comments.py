import pytest
from blogapp.blog.models import Post, Comment
from blogapp.blog.selectors.comment import post_comment_list

@pytest.fixture
def post():
    return Post.objects.create(title="Test Post", content="This is a test post.")


@pytest.fixture
def comments(post):
    parent_comment = Comment.objects.create(
        post=post, email="parent@example.com", text="This is a parent comment."
    )
    child_comment = Comment.objects.create(
        post=post,
        email="child@example.com",
        text="This is a child comment.",
        parent=parent_comment,
    )
    return parent_comment, child_comment

@pytest.mark.django_db
def test_post_comment_list(post, comments):
    parent_comment, child_comment = comments
    comments = post_comment_list(post_id=post.id)

    assert comments.count() == 2

    for comment in comments:
        assert comment.post == post
        if comment.parent:
            assert comment.parent == parent_comment
