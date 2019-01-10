from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user_id', 'title', 'body', 'url', 'comments')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'name',  'email', 'body', 'url')
