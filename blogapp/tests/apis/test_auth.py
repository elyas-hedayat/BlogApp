import json

import pytest
from blogapp.users.models import BaseUser
from django.test import Client
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_unauth_api():
    client = Client()

    url_ = reverse("blogapp.api:blog:post-list")

    response = client.get(url_, content_type="application/json")

    assert response.status_code == 200


@pytest.mark.django_db
def test_login():
    user = BaseUser.objects.create_user(email="js@js.com", password="js.sj")

    client = APIClient()
    url_ = reverse("blogapp.api:auth:login")
    body = {"email": user.email, "password": "js.sj"}
    response = client.post(url_, json.dumps(body), content_type="application/json")
    auth = json.loads(response.content)
    access = auth.get("access")
    refresh = auth.get("refresh")

    assert access != None
    assert type(access) == str

    assert refresh != None
    assert type(refresh) == str
