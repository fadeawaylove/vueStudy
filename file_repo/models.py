import logging
from django.db import models
from django.utils import timezone
# Create your models here.
from django.utils.safestring import mark_safe
from django.conf import settings

logger = logging.getLogger('log')

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


    def url(self):
        url_str = self.file_path.url
        return mark_safe(
            f"""
            <a href="{url_str}" target='blank' id="file_url">文件地址</a>
            <input type="button" onClick=copyToClip("{url_str}",1) value="复制">
            <input type="button" onClick=copyToClip("{url_str}",2) value="复制markdown格式">
            """ + 
            """ <script type="text/javascript">
            function copyToClip(content, copyType) {
                if(copyType === 1){
                    content = document.location.origin + content;
                }else{"""+
                    f"""content =  "![{self.name}](" + document.location.origin + content + ")";"""+"""
                }
                var aux = document.createElement("input"); 
                aux.setAttribute("value", content); 
                document.body.appendChild(aux); 
                aux.select();
                document.execCommand("copy"); 
                document.body.removeChild(aux);
                alert("复制成功");
                }
            </script>
            """
        )

    url.short_description = "跳转查看"
