from django.contrib import admin
from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'created_at')
    list_filter = ('user', 'post', 'created_at')
    search_fields = ('content', 'created_at')
    ordering = ('-created_at',)
