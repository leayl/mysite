from django.contrib import admin

from read_statistics.models import ReadNum


@admin.register(ReadNum)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("read_num", "content_type")
