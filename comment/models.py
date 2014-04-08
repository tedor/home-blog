from django.contrib.comments.models import Comment
from django.db import models
from django.utils.translation import ugettext_lazy as _

class ProtectComment(Comment):
    security_hash = models.CharField(_('security hash'), max_length=50, blank=True)
    timestamp = models.CharField(_('timestamp'), max_length=50, blank=True)
    headers_data = models.TextField(_('headers'), blank=True)
        
    class Meta:
        db_table = "django_comments_protect"
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        
    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
    
#    def save(self, *args, **kwargs):
#        super(Comment, self).save(*args, **kwargs)
#        
#    class Meta:
#        db_table = "django_comments"
#    class Meta:
#        super()