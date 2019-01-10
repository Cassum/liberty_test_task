from django.http import JsonResponse

from .models import Post

from .services.postsupdater import PostUpdater
from .services.commentsupdater import CommentUpdater


# Create your views here.
def index(request):
    PostUpdater().run()
    CommentUpdater().run()

    return JsonResponse([post.as_dict() for post in Post.objects.all()], safe=False)
