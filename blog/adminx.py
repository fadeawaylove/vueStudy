import xadmin


from .models import Post, Category, Tag


@xadmin.sites.register(Post)
class PostAdmin(object):
    list_display = ['title', 'create_time', 'update_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']
    list_filter = ["title", "category", "tags"]

    def save_models(self):
        self.new_obj.author = self.request.user
        super().save_models()

class CategoryAdmin(object):
    fields = ['name']
    list_filter = ["name"]

class TagAdmin(object):
    fields = ['name']
    list_filter = ["name"]

# xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)