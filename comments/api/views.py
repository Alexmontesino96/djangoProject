from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from comments.api.serializers import CommentsSerializer
from comments.api.permision import IsOwnerOrReadOnly


class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsOwnerOrReadOnly]


    



