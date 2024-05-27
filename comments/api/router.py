from rest_framework.routers import DefaultRouter
from comments.api.views import CommentsViewSet


router = DefaultRouter()
router.register(r'comments', CommentsViewSet, basename='comments')