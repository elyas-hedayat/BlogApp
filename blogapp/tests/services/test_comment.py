import pytest

from blogapp.blog.models import Comment, Post
from blogapp.blog.services.comment import comment_create
from blogapp.blog.services.post import post_create


@pytest.fixture
def post():
    return post_create(title="Test Post", content="This is a test post.")


@pytest.mark.django_db
def test_comment_create_without_parent(post):
    comment = comment_create(
        post=post.id, email="test@example.com", text="This is a test comment."
    )

    assert isinstance(comment, Comment)
    assert comment.post == post
    assert comment.email == "test@example.com"
    assert comment.text == "This is a test comment."
    assert comment.parent is None


@pytest.mark.django_db
def test_comment_create_with_parent(post):
    parent_comment = comment_create(
        post=post.id, email="parent@example.com", text="This is a parent comment."
    )

    child_comment = comment_create(
        post=post.id,
        email="child@example.com",
        text="This is a child comment.",
        parent=parent_comment.id,
    )

    assert isinstance(child_comment, Comment)
    assert child_comment.post == post
    assert child_comment.email == "child@example.com"
    assert child_comment.text == "This is a child comment."
    assert child_comment.parent == parent_comment
