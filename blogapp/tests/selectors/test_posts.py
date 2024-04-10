import pytest

from blogapp.blog.selectors.post import post_list


@pytest.mark.django_db
def test_post_list():
    posts = post_list()
    assert posts.count() == 0
