import json

import pytest
from devopshobbies.blog.models import Post
from devopshobbies.users.models import BaseUser
from django.urls import reverse


@pytest.mark.django_db
def test_empty_post_api(api_client, user1, subscription1, profile1, post1):
    url_ = reverse("api:blog:post")

    response = api_client.get(url_, content_type="application/json")
    data = json.loads(response.content)

    assert response.status_code == 200
    assert data.get("results") == []
    assert data.get("limit") == 10
