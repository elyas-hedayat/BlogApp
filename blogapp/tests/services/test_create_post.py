import pytest
from blogapp.blog.services.post import post_create


@pytest.mark.django_db
def test_create_post():
    post_instance = post_create(title="pooo", content="CCCContent")
    assert post_instance.title == "pooo"
    assert post_instance.content == "CCCContent"
