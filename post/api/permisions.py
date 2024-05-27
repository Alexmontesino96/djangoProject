from rest_framework import permissions
from post.models import Post


class IsAdminUserOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        elif request.method == 'PUT':
            slug = request.data.get('slug')
            post = Post.objects.get(slug=slug)
            if request.user.is_staff or request.user == post.user:
                return True
            else:
                return False

        else:
            return request.user.is_staff


