from django.contrib.contenttypes.models import ContentType

from django.db import models
from django.db.models.fields import exceptions
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

from read_statistics.models import ReadNumExtendMethod


class BlogType(models.Model):
    title = models.CharField(max_length=32)
    def __str__(self):
        return self.title

class Blog(models.Model,ReadNumExtendMethod):
    title = models.CharField(max_length=32)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # read_times = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-created_time']



'''
class ReadNum(models.Model):
    read_num=models.IntegerField(default=0)
    blog=models.OneToOneField(Blog,on_delete=models.DO_NOTHING)
'''