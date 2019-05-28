"""
Sitemap 可方便网站管理员通知搜索引擎他们网站上有哪些可供抓取的网页。
最简单的 Sitemap 形式，就是XML 文件，在其中列出网站中的网址以及关于每个网址的其他元数据（
上次更新的时间、更改的频率以及相对于网站上其他网址的重要程度为何等），以便搜索引擎可以更加智能地抓取网站。
"""
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post

class PostSitemap(Sitemap):
    changefrep = 'always'
    property = 1.0
    protocol = 'https'

    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)

    def lastmod(self,obj):
        return obj.created_time

    def location(self, obj):
        return reverse('post-detail',args=[obj.pk])