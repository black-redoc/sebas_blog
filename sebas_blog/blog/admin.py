from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["blog_title", "blog_content", "blog_author", "created_at"]
    search_fields = ["blog_title", "blog_author"]
