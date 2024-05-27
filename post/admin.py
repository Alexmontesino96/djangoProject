from django.contrib import admin
from post.models import Post


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'published')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'content')
