from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    title = models.TextField()
    body = models.TextField()


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_query_name='comments',
    )
    name = models.TextField()
    email = models.EmailField()
    body = models.TextField()
