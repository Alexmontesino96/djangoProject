from django.contrib import admin
from categories.models import Categories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')
    list_filter = ('published',)
