from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
