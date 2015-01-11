from django.contrib.syndication.views import Feed
from blog.models import Post
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from content.utils import get_site_name

class LatestEntriesFeed(Feed):
    title = "%s - %s" % (get_site_name(), unicode(_("blog")))
    description = _("Latest posts from blog page")

    def link(self):
        return reverse('blog_feeds')

    def items(self):
        return Post.objects.filter(status=Post.STATUS_PUBLIC).order_by('-created_at')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.get_text_cut

    def item_link(self, item):
        return item.get_absolute_url()

    def item_pubdate(self, item):
	    return item.updated_at

class LatestTagEntriesFeed(LatestEntriesFeed):
    tag = ''

    def get_object(self, request, tag):
        self.tag = tag
        self.description = _("Latest posts from blog page by tag") + ': ' + tag;
        self.title = "%s - %s" % (get_site_name(), unicode(_("blog"))) + ': ' + tag;

    def items(self):
        return Post.objects.filter(status=Post.STATUS_PUBLIC, tag__contains=self.tag).order_by('-created_at')[:10]