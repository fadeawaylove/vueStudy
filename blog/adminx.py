import xadmin

from import_export import resources
from xadmin import views
from .models import Post, Category, Tag



class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        # 导入数据时，如果该条数据未修改过，则会忽略
        skip_unchanged = True
        # 在导入预览页面中显示跳过的记录
        report_skipped = True
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id
        import_id_fields = ('id',)

        fields = (
            'id',
            'title',
            'body',
        )
        # 白名单

        # 黑名单
        exclude = (
            'create_time',
            'update_time',
        )


@xadmin.sites.register(Post)
class PostAdmin(object):
    list_display = ['title', 'post_address', 'category', 'author', 'status', 'create_time', 'update_time']
    fields = ['title', 'body', 'status', 'excerpt', 'category', 'tags']
    list_filter = ["title", "category", "tags", 'status']

    # 列表可直接修改的字段
    # list_editable = ['title', 'category']

    import_export_args = {
        'import_resource_class': PostResource,
    }

    def save_models(self):
        self.new_obj.author = self.request.user
        super().save_models()

class CategoryAdmin(object):
    fields = ['name']
    list_filter = ["name"]

class TagAdmin(object):
    fields = ['name']
    list_filter = ["name"]


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)