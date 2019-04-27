from django.contrib import admin
from .models import BlogType, Blog


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id","get_read_num","title", "blog_type", "author", "created_time", "last_update_time")

'''
@admin.register(ReadNum)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("read_num", "blog")
'''