from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import settings
from content.feeds import LatestEntriesFeed

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^blog/', include('blog.urls')),
    url(r'^content/', include('content.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login_page'),

    # Global static content
    url(r'^comments/', include('django.contrib.comments.urls')),     
    url(r'^feeds/$', LatestEntriesFeed(), name='home_feeds'),  
    url(r'^robots\.txt$', 'content.views.robots', name='robot_txt'),  
    url(r'^o/$', 'content.views.about', name='about_page'), 
    url(r'^developers/$', 'content.views.developers', name='developers_page'),
    url(r'^$', 'content.views.home', name='home_page'),

)

#if settings.DEBUG:
#urlpatterns += patterns('django.contrib.staticfiles.views',
#    url(r'^static/(?P<path>.*)$', 'serve'),
#    url(r'^media/(?P<path>.*)$', 'serve'),
#)

