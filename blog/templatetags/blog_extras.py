from django import template
from django.db.models import Q
from django.db.models.aggregates import Count

from ..models import *

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Post.objects.filter(status=1).order_by('-create_time')[:num],
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.filter(status=1).dates('create_time', 'month', order='DESC'),
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    category_list = Category.objects.filter(post__status=1).annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return {
        'category_list': category_list
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    tag_list = Tag.objects.filter(post__status=1).annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return {
        'tag_list': tag_list
    }
