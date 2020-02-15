from django.db import models
from django.utils import timezone
# Create your models here.
from django.utils.safestring import mark_safe
from django.conf import settings


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
        url_str = '"' + self.file_path.url + '"'
        return mark_safe(
            """
            <a href=""" + url_str + """ target='blank' id="file_url">文件地址</a>
            <input type="button" onClick=copyToClip(""" + url_str + """) value="复制">
            <script type="text/javascript">
            function copyToClip(content, message) {
                content = document.location.origin + content
                var aux = document.createElement("input"); 
                aux.setAttribute("value", content); 
                document.body.appendChild(aux); 
                aux.select();
                document.execCommand("copy"); 
                document.body.removeChild(aux);
                if (message == null) {
                    alert("复制成功");
                } else{
                    alert(message);
                }
                }
            </script>
            """
        )

    url.short_description = "跳转查看"

    def copy_url(self):
        return mark_safe(
            """
            <input type="button" id="url_copy" onClick='copyLink()' value="复制url地址"></input>
            <script type="text/javascript">
            function copyLink(){
                var e = document.getElementById("url_copy");
                e.select(); // 选择对象
                console.log(e.select())
                document.execCommand("Copy"); // 执行浏览器复制命令
                alert("内容复制成功！");
            }
            </script>
            """
        )

    copy_url.short_description = "复制url"