import json

import requests

from django.db.transaction import atomic

from postscomments.models import Post


class PostUpdater:
    _url = 'https://jsonplaceholder.typicode.com/posts'

    @atomic
    def run(self):
        data = requests.get(self._url).json()
        for record in data:
            post = Post(
                id=record['id'],
                user_id=record['userId'],
                title=record['title'],
                body=record['body'],
            )
            post.save()
