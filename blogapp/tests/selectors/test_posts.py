import pytest
from blogapp.blog.selectors.post import post_list


@pytest.mark.django_db
def test_post_list(post1):
    a = post_list()
    assert a.first() == post1
