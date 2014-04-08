from __future__ import absolute_import

from . import admin_views
from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^picture_blog_list', admin_views.blog_list, name='picture_blog_list'),
    url(r'^picture_blog_upload', admin_views.blog_uload, name='picture_blog_upload'),
    url(r'^piture_blog_delete/(\d+)', admin_views.blog_delete, name='picture_blog_delete')
)

