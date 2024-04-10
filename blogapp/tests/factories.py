import factory
from blogapp.blog.models import Post
from blogapp.tests.utils import faker
from blogapp.users.models import BaseUser
from django.utils import timezone


class BaseUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BaseUser

    email = factory.Iterator(["fr@gmail.com", "it@gmail.com", "es@gmail.com"])
    password = factory.PostGenerationMethodCall("set_password", "adm1n")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.LazyAttribute(lambda _: f"{faker.unique.company()}")
    content = factory.LazyAttribute(lambda _: f"{faker.unique.company()}")
    created_at = factory.LazyAttribute(lambda _: f"{timezone.now()}")
    updated_at = factory.LazyAttribute(lambda _: f"{timezone.now()}")
