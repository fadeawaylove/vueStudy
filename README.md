### 一个轻量的个人博客

博客地址：[https://dog.fadeaway.ltd/](https://dog.fadeaway.ltd/)

#### 简介
> 使用Django作为后台服务，前端页面从[模板之家](http://www.cssmoban.com/)采集，使用的前后端不分离模式。后台管理使用的xadmin，整合了mdeditor实现markdown文本的编辑。

------------------
#### 首页

![v2ray配置截图](https://dog.fadeaway.ltd/media/2020/05/06/dogBlog%E5%8D%9A%E5%AE%A2%E9%A6%96%E9%A1%B5.png)

左侧展示最新的文章，右侧分别展示最新、归档、分类、标签以及RSS订阅。

----------------------------------
#### 阅读页
![v2ray配置截图](https://dog.fadeaway.ltd/media/2020/05/06/c.png)


左侧为博客内容，右侧新增了文章目录，底部是评论功能。除此之外，后台将markdown博客转化为html进行前端页面展示，同时前端页面还集成了latex公式展示功能。

--------------------
#### 后台管理页面
![v2ray配置截图](https://dog.fadeaway.ltd/media/2020/05/06/%E5%90%8E%E5%8F%B0%E7%AE%A1%E7%90%86%E9%A1%B5%E9%9D%A2.png)

后台管理页面就是xadmin实现的，实现简单的后台管理功能，对文章、分类、标签进行管理，同时还新增了一个附件功能，用来上传文件或者图片等资源，其中图片可用作markdown写作使用。

