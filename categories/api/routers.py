from rest_framework.routers import DefaultRouter
from categories.api.views import CategoriesApiViewSet

router = DefaultRouter()
router.register("categories", CategoriesApiViewSet, basename="categories")