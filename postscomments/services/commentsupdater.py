import requests

from django.db.transaction import atomic

from postscomments.models import Comment, Post


class CommentUpdater:
    _url = 'https://jsonplaceholder.typicode.com/comments'

    @atomic
    def run(self):
        data = requests.get(self._url).json()
        for record in data:
            comment = Comment(
                id=record['id'],
                post=Post(id=record['postId']),
                name=record['name'],
                email=record['email'],
                body=record['body'],
            )
            comment.save()
