from django.db import models


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    title = models.TextField()
    body = models.TextField()

    def __str__(self):
        return f'<Post {self.id} {self.title}>'

    def as_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'title': self.title,
            'body': self.body,
            'comments': [comment.as_dict() for comment
                         in self.comments.all()],
        }


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    name = models.TextField()
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f'<Comment {self.id} {self.post.id}>'

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'body': self.body,
        }
