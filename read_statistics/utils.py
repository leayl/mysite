"""
根据具体对象更改阅读计数，
可用于多个app内的models对象
"""

from django.contrib.contenttypes.models import ContentType
from django.db.models.fields import exceptions
from read_statistics.models import ReadNum


def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj) # 根据obj获取其对应Model
    key = "%s_%s_pk" % (ct.model, obj.pk) # 根据obj获取其对应Model的title、obj的pk，组成对应cookie的键值
    if not request.COOKIES.get(key):
        try:
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        except exceptions.ObjectDoesNotExist:
            readnum = ReadNum(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()
    return key
