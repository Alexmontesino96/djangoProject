from rest_framework.serializers import ModelSerializer
from categories.models import Categories


class CategoriesSerializer(ModelSerializer):

    class Meta:
        model = Categories
        fields = ["id", "title", "slug", "published"]
