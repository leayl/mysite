from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType

from blog.models import Blog
from read_statistics.utils import get_weekly_days_read_data

def home(request):
    """
    获取近一周的阅读数量，以图表的形式显示在首页
    :param request:
    :return:
    """
    blog_content_type = ContentType.objects.get_for_model(Blog)
    read_nums,dates = get_weekly_days_read_data(blog_content_type)
    context={}
    context["read_nums"]=read_nums
    context["dates"]=dates
    return render(request,"home.html",context)