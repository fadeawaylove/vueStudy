import logging
import xadmin


from .models import Post, Category, Tag, ExtraSection


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

@xadmin.sites.register(ExtraSection)
class ExtraSectionAdmin(object):
    list_display = ["section_title", "section_base_description", "section_name","section_img", "update_time"]
    fields = ["section_title", "section_base_description", "section_name","section_img"]
    list_filter = ["section_title"]

# xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)