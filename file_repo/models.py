from django.db import models
from django.utils import timezone
# Create your models here.

class FileManager(models.Model):
    """
    文件上传管理的类
    """
    name = models.CharField('文件名',max_length=200)
    file_path = models.FileField('文件路径',upload_to="%Y/%m/%d/")
    create_time = models.DateTimeField("创建时间", default=timezone.now)
    update_time = models.DateTimeField("修改时间")

    class Meta:
        verbose_name = '附件'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def save(self, *args, **kwargs):
        self.update_time = timezone.now()
        super().save(*args, **kwargs)
