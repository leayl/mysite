from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.fields import exceptions
from django.utils import timezone


class ReadNum(models.Model):
    """
    统计每个模型对应数据的总共阅读数量
    """
    read_num = models.IntegerField(default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING) # 模型类
    object_id = models.PositiveIntegerField() # 模型类的具体对象
    content_object = GenericForeignKey("content_type", "object_id")


class ReadNumExtendMethod():
    """
    获取继承此类的子类的实例的总共阅读量
    """
    def get_read_num(self):
        ct = ContentType.objects.get_for_model(self)
        try:
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0

class ReadDetail(models.Model):
    """
    统计每个模型对应数据的每日阅读量
    """
    date = models.DateField(default=timezone.now)
    read_num = models.IntegerField(default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)  # 模型类
    object_id = models.PositiveIntegerField()  # 模型类的具体对象
    content_object = GenericForeignKey("content_type", "object_id")