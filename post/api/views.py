from rest_framework.viewsets import ModelViewSet
from post.api.serializers import PostSerializers, CreatePostSerializers
from post.models import Post
from django_filters.rest_framework import DjangoFilterBackend
from post.api.permisions import IsAdminUserOrReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published', 'categories__slug', 'categories']
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreatePostSerializers
        return PostSerializers

