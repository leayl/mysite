from django.contrib import admin
from .models import BlogType, Blog


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "blog_type", "author","read_times", "created_time", "last_update_time")
