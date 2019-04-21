from django.shortcuts import get_object_or_404, render
from blog.models import Blog, BlogType
from django.core.paginator import Paginator
from django.conf import settings


def blog_list(request):
    # 获取页码参数
    page_num = request.GET.get("page", 1)
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, settings.EACH_PAGE_BLOGS_NUMBER)
    page_of_blogs = paginator.get_page(page_num)  # 如果page不是数字字符会自动返回第一页
    current_page_num = page_of_blogs.number
    # 获取当前页码前后各两页的页码范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min((paginator.num_pages, current_page_num + 2))+1))
    # 加上省略号
    if page_range[0]-1 >= 2:
        page_range.insert(0,'...')
    if page_range[-1] <= paginator.num_pages-2:
        page_range.append('...')
    # 加上首尾页码
    if page_range[0] != 1:
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = {}
    context["page_of_blogs"] = page_of_blogs  # 将获取页面对象返回前端
    context["page_range"] = page_range  # 分页显示的页码范围
    context["blog_types"] = BlogType.objects.all()

    return render(request, "blog/blog_list.html", context)


def blog_detail(request, blog_pk):
    context = {}
    context["blog"] = get_object_or_404(Blog, pk=blog_pk)
    return render(request, "blog/blog_detail.html", context)


def blogs_with_type(request, blog_type_pk):
    # 获取页码参数
    page_num = request.GET.get("page", 1)
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs = Blog.objects.filter(blog_type=blog_type)
    paginator = Paginator(blogs, settings.EACH_PAGE_BLOGS_NUMBER)
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
    context = {}
    context["page_of_blogs"] = page_of_blogs  # 将获取页面对象返回前端
    context["page_range"] = page_range  # 分页显示的页码范围
    context["blog_type"] = blog_type
    context["blog_types"] = BlogType.objects.all()
    return render(request, "blog/blogs_with_type.html", context)
