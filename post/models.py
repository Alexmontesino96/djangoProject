from django.db import models
from django.db.models import SET_NULL


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    miniature = models.ImageField(upload_to='post/miniatures/', null=True, blank=True)
    user = models.ForeignKey('user.User', on_delete=SET_NULL, null=True)
    published = models.BooleanField(default=False)
    categories = models.ForeignKey('categories.Categories', on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.title
