from __future__ import absolute_import
from django.conf.urls.defaults import url, patterns
from . import views
from blog.feeds import LatestEntriesFeed, LatestTagEntriesFeed
from blog.sitemap import BlogSitemap

sitemaps = { 
    'blog':BlogSitemap
}

urlpatterns = patterns('',
    url(r'^feeds$', LatestEntriesFeed(), name='blog_feeds'),
    url(r'^feeds/tag/(?P<tag>.+)', LatestTagEntriesFeed(), name='post_list_by_tag_feeds'),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}, name='blog_sitemap'),
    url(r'^taglookup$', views.tag_lookup, name='blog_tag_lookup'),
    url(r'^(?P<slug>[-\w]+)$', views.post_detail, name='blog_post_detail'),
    url(r'^tag/(?P<tag>.+)$', views.post_list_by_tag, name='post_list_by_tag'),
    url(r'^$', views.post_list, name='blog_page'),
)