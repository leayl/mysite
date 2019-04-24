from django.shortcuts import get_object_or_404, render, render_to_response
from blog.models import Blog, BlogType
from django.core.paginator import Paginator
from django.conf import settings


def get_blog_list_common_data(request,blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)
    page_num = request.GET.get("page", 1)
    page_of_blogs = paginator.get_page(page_num)  # 如果page不是数字字符会自动返回第一页
    current_page_num = page_of_blogs.number
    # 获取当前页码前后各两页的页码范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min((paginator.num_pages, current_page_num + 2)) + 1))
    # 加上省略号
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if page_range[-1] <= paginator.num_pages - 2:
        page_range.append('...')
    # 加上首尾页码
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    blog_dates =  Blog.objects.dates('created_time', 'day', order='DESC')
    # 获取日期分类的数量
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count =  Blog.objects.filter(created_time__year=blog_date.year,
                                     created_time__month=blog_date.month,
                                     created_time__day=blog_date.day,
                                     ).count()
        blog_dates_dict[blog_date]=blog_count
    context = {}
    context["page_of_blogs"] = page_of_blogs  # 将获取页面对象返回前端
    context["page_range"] = page_range  # 分页显示的页码范围
    context["blog_types"] = BlogType.objects.all()
    context["blog_dates"] =blog_dates_dict
    return context

def blog_list(request):
    # 获取页码参数
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request,blogs_all_list)
    return render(request, "blog/blog_list.html", context)


def blogs_with_type(request, blog_type_pk):
    # 获取页码参数
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request,blogs_all_list)
    context["blog_type"] = blog_type
    return render(request, "blog/blogs_with_type.html", context)


def blogs_with_date(request, year, month, day):
    blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month, created_time__day=day)
    context = get_blog_list_common_data(request,blogs_all_list)
    context["blogs_with_date"] = "%s年%s月%s日" % (year, month, day)
    return render(request, "blog/blogs_with_date.html", context)



def blog_detail(request, blog_pk):
    context = {}
    blog = get_object_or_404(Blog, pk=blog_pk)
    # 为博客阅读计数
    if not request.COOKIES.get("blog_%s_read" % blog.pk):
        blog.read_times += 1
    blog.save()
    context["blog"] = blog
    context["previous_blog"] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context["next_blog"] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context["blog_dates"] = Blog.objects.dates('created_time', 'day', order='DESC')
    response = render_to_response("blog/blog_detail.html", context)
    response.set_cookie("blog_%s_read" % blog.pk,"true")
    return response
