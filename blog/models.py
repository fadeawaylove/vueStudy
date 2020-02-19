import markdown
import re

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.html import strip_tags
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from django.utils.functional import cached_property
from mdeditor.fields import MDTextField
from django.utils.safestring import mark_safe


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField("标题",max_length=100)
    # body = models.TextField("正文")
    body = MDTextField()
    create_time = models.DateTimeField("创建时间", default=timezone.now)
    update_time = models.DateTimeField("修改时间")
    excerpt = models.CharField("摘要",max_length=200, blank=True)
    category = models.ForeignKey(Category,verbose_name="分类",on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name="标签",blank=True)
    author = models.ForeignKey(User, verbose_name="作者",on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def save(self, *args, **kwargs):
        self.update_time = timezone.now()
        # 首先实例化一个 Markdown 类，用于渲染 body 的文本。
        # 由于摘要并不需要生成文章目录，所以去掉了目录拓展。
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
 
        # 先将 Markdown 文本渲染成 HTML 文本
        # strip_tags 去掉 HTML 文本的全部 HTML 标签
        # 从文本摘取前 54 个字符赋给 excerpt
        self.excerpt = strip_tags(md.convert(self.body))[:54]

        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.pk})

    def post_address(self):
        return mark_safe("<a href=" "'" + self.get_absolute_url() + "'"+ " target='blank'>查看文章</a>")

    post_address.short_description="文章地址"

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    
    @property
    def toc(self):
        return self.rich_content.get("toc", "")
 
    @property
    def body_html(self):
        return self.rich_content.get("content", "")
 
    @cached_property
    def rich_content(self):
        return generate_rich_content(self.body)

    def __str__(self):
        return self.title


def generate_rich_content(value):
    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            # 记得在顶部引入 TocExtension 和 slugify
            TocExtension(slugify=slugify),
        ]
    )
    content = md.convert(value)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    toc = m.group(1) if m is not None else ""
    return {"content": content, "toc": toc}


# class ExtraSection(models.Model):
#     """
#     额外的板块
#     """
#
#     section_title = models.CharField("板块标题", max_length=100)
#     section_base_description = models.CharField("基本描述", max_length=256)
#     section_name = models.CharField("板块名", max_length=20, help_text="用于帮助页面组合板块详情对应的url")
#     section_img = models.CharField("封面图片地址", max_length=200, blank=True)
#
#     create_time = models.DateTimeField("创建时间", default=timezone.now)
#     update_time = models.DateTimeField("修改时间")
#
#     class Meta:
#         verbose_name = '更多板块'
#         verbose_name_plural = verbose_name
#         ordering = ['-create_time']
#
#     def save(self, *args, **kwargs):
#         self.update_time = timezone.now()
#         super().save(*args, **kwargs)
#
#
#     def get_absolute_url(self):
#         return reverse("{}:index".format(self.section_name))

