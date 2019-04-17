from django.shortcuts import get_object_or_404,render
from blog.models import Blog, BlogType


def blog_list(request):
    context={}
    context["blogs"]=Blog.objects.all()
    return render(request,"blog/blog_list.html",context)

def blog_detail(request,blog_pk):
    context={}
    context["blog"]=get_object_or_404(Blog,pk=blog_pk)
    return render(request,"blog/blog_detail.html",context)


def blogs_with_type(request,blog_type_pk):
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    context={}
    context["blogs"]=Blog.objects.filter(blog_type=blog_type)
    context["blog_type"]=blog_type
    return render(request,"blog/blogs_with_type.html",context)