from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from content.views import get_all_data
from content.utils import get_site_name

class LatestEntriesFeed(Feed):
    title = "%s - %s" % (get_site_name(), unicode(_("all feeds")))
    description = _("Latest news from all pages")
    
    def link(self):
        return reverse('home_feeds')
        
    def items(self):
        return get_all_data()
    
    def item_title(self, item):
        return item['title']

    def item_description(self, item):
        return item['text']
    
    def item_link(self, item):
        return item['url']