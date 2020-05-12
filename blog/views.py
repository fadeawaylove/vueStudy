from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from pure_pagination.mixins import PaginationMixin
from django.db.models import Q
from django.http import HttpResponse

from .models import *


# Create your views here.
class IndexView(PaginationMixin, ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-create_time')


class CategoryView(IndexView):

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


class ArchivesView(IndexView):

    def get_queryset(self):
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")
        return super(ArchivesView, self).get_queryset().filter(create_time__year=year, create_time__month=month)


class TagView(IndexView):

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
        return post


def search(request):
    q = request.GET.get("q")
    if not q:
        error_msg = "请输入搜索关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
        return redirect('blog:index')
    post_list = Post.objects.filter((Q(title__icontains=q) | Q(body__icontains=q)) & Q(status=1))
    return render(request, 'blog/index.html', {'post_list': post_list})
