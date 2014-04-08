from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from tagging.fields import TagField
from django.utils import timezone

class Post(models.Model):
    STATUS_DRAFT = 1
    STATUS_PUBLIC = 2

    TEXT_CUT = "===cut==="
    
    STATUS_CHOICES = (
        (STATUS_DRAFT, _('Draft')),
        (STATUS_PUBLIC, _('Public')),
    )
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), unique=True)
    text = models.TextField(_('text'), help_text="<a href='http://daringfireball.net/projects/markdown/syntax'>Markdown</a>")
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)
    tag = TagField()
    
    def save(self):
        if not self.created_at:
            self.created_at = timezone.now()
            
        super(Post, self).save()

    def __unicode__(self):
        return self.title
    
    @property
    def get_text_cut(self):
        return u'%s' % self.text.split(Post.TEXT_CUT)[0]

    @property
    def get_text(self):
        return u'%s' % self.text.replace(Post.TEXT_CUT, "")

    @permalink
    def get_absolute_url(self):
        return ('blog_post_detail', None, {'slug': self.slug})