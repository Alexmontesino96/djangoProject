from rest_framework.viewsets import ModelViewSet
from categories.models import Categories
from categories.api.serializers import CategoriesSerializer
from rest_framework.permissions import IsAuthenticated
from categories.api.permision import IsAdminReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CategoriesApiViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [IsAdminReadOnly]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published', 'title']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Categories.objects.all()
        else:
            return Categories.objects.filter(published=True)




