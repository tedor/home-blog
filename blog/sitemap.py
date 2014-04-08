from blog.models import Post
from django.contrib.sitemaps import Sitemap

class BlogSitemap(Sitemap):
    def items(self):
        return Post.objects.filter(status=Post.STATUS_PUBLIC).order_by('-created_at')

    def lastmod(self, obj):
        return obj.created_at