from rest_framework.serializers import ModelSerializer, SlugRelatedField
from post.models import Post
from user.api.serializer import UserSerializer
from categories.api.serializers import CategoriesSerializer
from categories.models import Categories


class PostSerializers(ModelSerializer):
    user = UserSerializer()
    categories = CategoriesSerializer()

    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'created_at', 'miniature', 'user', 'published', 'categories']


class CreatePostSerializers(ModelSerializer):
    categories = SlugRelatedField(slug_field='slug', queryset=Categories.objects.all())
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'published', 'categories']
