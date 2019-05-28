from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed
from .models import Post



'''
RSS搭建了信息迅速传播的一个技术平台，使得每个人都成为潜在的信息提供者。
发布一个RSS文件后，这个RSS Feed中包含的信息就能直接被其他站点调用，而且由于这些数据都是标准的XML格式，
所以也能在其他的终端和服务中使用，是一种描述和同步网站内容的格式。
'''

class ExtendedRSSFeed(Rss201rev2Feed):
    def add_item_elements(self, handler, item):
        super(ExtendedRSSFeed,self).add_item_elements(handler,item)
        handler.addQuickElement('content:html',item['content_html'])






class LatestPostFeed(Feed):
    feed_type = ExtendedRSSFeed
    titile = 'Typeidea Blog System'
    link = '/rss/'
    description = 'typeidea is a blog system power by django'

    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.desc

    def item_link(self, item):
        return reverse('post-detail',args=[item.pk])

    def item_extra_kwargs(self, item):
        return {'content_html':self.item_content_html(item)}

    def item_content_html(self,item):
        return item.content_html







