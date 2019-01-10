from django.http import JsonResponse
from rest_framework import viewsets

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .services.postsupdater import PostUpdater
from .services.commentsupdater import CommentUpdater


# Create your views here.
def index(request):
    PostUpdater().run()
    CommentUpdater().run()
    return JsonResponse(
        [post.as_dict() for post in Post.objects.all()],
        safe=False,
    )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
