import re
import markdown

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
from markdown.extensions.toc import TocExtension

from .models import *

# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"

class CategoryView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

class ArchivesView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"

    def get_queryset(self):
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")
        return super(ArchivesView, self).get_queryset().filter(create_time__year=year, create_time__month=month)

class TagView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"

    def get_queryset(self):
        tag_id = self.kwargs.get("pk")
        tag = get_object_or_404(Tag, pk=tag_id)
        return super().get_queryset().filter(tags=tag)

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super().get_object(queryset=queryset)
        md = markdown.Markdown(extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    #   'markdown.extensions.toc',
                                    TocExtension(slugify=slugify)
                                    ])
        post.body = md.convert(post.body)
        m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
        post.toc = m.group(1) if m else ""
        return post

# def index(request):
#     post_list = Post.objects.all().order_by("-create_time")
    
#     return render(request,"blog/index.html", context={
#         "post_list": post_list
#     })


# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.increase_views()
#     md = markdown.Markdown(extensions=[
#                                       'markdown.extensions.extra',
#                                       'markdown.extensions.codehilite',
#                                       #   'markdown.extensions.toc',
#                                         TocExtension(slugify=slugify)
#                                       ])
#     post.body = md.convert(post.body)
#     m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
#     post.toc = m.group(1) if m else ""
#     return render(request, 'blog/detail.html', context={'post': post})


# def archives(request, year, month):
#     post_list = Post.objects.filter(create_time__year=year,
#                                     create_time__month=month).order_by("-create_time")
#     return render(request, "blog/index.html", context={'post_list': post_list})

# def category(request, pk):
#     cate = get_object_or_404(Category, pk=pk)
#     post_list = Post.objects.filter(category=cate).order_by("-create_time")
#     return render(request, "blog/index.html", context={'post_list': post_list})

# def tag(request, pk):
#     t = get_object_or_404(Tag, pk=pk)
#     post_list = Post.objects.filter(tags=t).order_by("-create_time")
#     return render(request, "blog/index.html", context={'post_list': post_list})