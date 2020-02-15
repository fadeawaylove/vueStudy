import xadmin
from .models import FileManager

@xadmin.sites.register(FileManager)
class FileRepoAdmin(object):
    list_display = ['name', 'file_path',"url", 'create_time', 'update_time']
    fields = ['name', 'file_path']
    list_filter = ["name", "file_path"]

