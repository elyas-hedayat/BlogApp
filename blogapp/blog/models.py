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


class Comment(models.Model):
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.text
