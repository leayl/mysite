"""
根据具体对象更改阅读计数，
可用于多个app内的models对象
"""

import datetime
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum

from read_statistics.models import ReadNum, ReadDetail
from django.utils import timezone


def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)  # 根据obj获取其对应Model
    key = "%s_%s_pk" % (ct.model, obj.pk)  # 根据obj获取其对应Model的title、obj的pk，组成对应cookie的键值
    if not request.COOKIES.get(key):
        # 总阅读数量+1
        # 不存在则创建
        readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()

        # 当日阅读数量+1
        date = timezone.now()
        readDetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        readDetail.read_num += 1
        readDetail.save()
    return key


def get_weekly_days_read_data(content_type):
    today = timezone.now().date()
    read_nums = []
    dates = []
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime("%m/%d"))
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum("read_num"))  # {"read_num_sum":聚合后的结果}
        read_nums.append(result['read_num_sum'] or 0)
    return read_nums,dates
