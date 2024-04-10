from django.db import models

from blogapp.common.models import BaseModel


class Post(BaseModel):
    title = models.CharField(
        max_length=200,
    )
    content = models.CharField(
        max_length=1000,
    )

    def __str__(self):
        return self.title
