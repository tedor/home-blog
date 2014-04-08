from django.contrib.comments.forms import CommentForm
from django.utils.translation import ugettext_lazy as _
import settings
import datetime
from django.utils.encoding import force_unicode
from django.contrib.contenttypes.models import ContentType
from comment.models import ProtectComment
from django.forms.util import ErrorDict

class CommentFormCustom(CommentForm):
    
    def __init__(self, target_object, data=None, initial=None):
        super(CommentFormCustom, self).__init__(target_object, data, initial) 
        self.fields['name'].label = _("Your name/email/nick")
        
    def security_errors(self):
        """Return just those errors associated with security"""
        errors = ErrorDict()
        for f in ["honeypot", "timestamp", "security_hash", "db_security_hash"]:
            if f in self.errors:
                errors[f] = self.errors[f]
        
        if not self.clean_db_security_hash():
            errors["db_security_hash"] = "Security hash is already exists."
        return errors

    def clean_db_security_hash(self):
        return self.get_comment_model()._default_manager.using(
            self.target_object._state.db
        ).filter(           
            security_hash = self.data.get("security_hash")
        ).count() is 0

    def get_comment_create_data(self):
        # Use the data of the superclass, and remove extra fields
        return dict(
            content_type = ContentType.objects.get_for_model(self.target_object),
            object_pk    = force_unicode(self.target_object._get_pk_val()),
            user_name    = self.cleaned_data["name"],
            comment      = self.cleaned_data["comment"],
            security_hash = self.cleaned_data["security_hash"],
            timestamp    = self.cleaned_data["timestamp"],
            submit_date  = datetime.datetime.now(),
            site_id      = settings.SITE_ID,
            is_public    = False,
            is_removed   = False,
        )

    def get_comment_model(self):
        return ProtectComment
    
CommentFormCustom.base_fields.pop('url')
CommentFormCustom.base_fields.pop('email')