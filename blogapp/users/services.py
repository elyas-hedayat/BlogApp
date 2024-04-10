from django.db import transaction
from .models import BaseUser, Profile


def create_user(*, email: str, password: str) -> BaseUser:
    return BaseUser.objects.create_user(email=email, password=password)
