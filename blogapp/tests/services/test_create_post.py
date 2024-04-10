import pytest
from blogapp.blog.services.post import create_post


@pytest.mark.django_db
def test_create_post(post1):
    a = create_post(title="pooo", content="CCCContent")

    assert a.title == "pooo"
    assert a.content == "CCCContent"
