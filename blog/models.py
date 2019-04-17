from django.db import models
from django.contrib.auth.models import User


class BlogType(models.Model):
    title = models.CharField(max_length=32)
    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=32)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title