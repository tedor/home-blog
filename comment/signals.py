from django.contrib.sites.models import get_current_site
from django.core.mail import mail_admins
from email import Charset
from django.core.urlresolvers import reverse
from django.contrib import comments
from django.contrib.comments.views.comments import CommentPostBadRequest
import re
from blog.utils import validate_hash

def save_name_to_cookie(sender, comment, request, **kwargs):    
#    response = HttpResponse()
#    response.set_cookie('comment_user_name', comment.name)
#    return response
    pass
#    request.session['comment_user_name'] = comment.name


def send_to_email(sender, comment, request, **kwargs):
    Charset.add_charset('utf-8', Charset.SHORTEST, None, 'utf-8')
    root_url = "http://%s" % get_current_site(request)    
    
    subject = 'New comments from - %s' % comment.user_name
    url = '%s/admin/comments/comment/%d' % (root_url, comment.id)
    message = 'Author: %s\n\n' % comment.user_name
    message += '%s\n\n' % comment.comment    
    message += 'Posted by: %s\n' % comment.submit_date.strftime('%Y-%m-%d %H:%S')
    message += 'Comment url: %s\n' % url
    message += 'Post url: %s%s' % (root_url, comment.content_object.get_absolute_url())
    message += '\n\nApprove url: %s/comments%s' % (root_url, reverse('comments-approve', comments.urls, [comment.id]))
    message += '\nDelete url: %s/comments%s' % (root_url, reverse('comments-delete', comments.urls, [comment.id]))
    
    try:
        mail_admins(subject, message)
    except:
        pass
    
def check_meta_data(sender, comment, request, **kwargs):
    protect_data = {}
    for meta in request.META:
        if re.match("HTTP_X_P_G_*", meta):
            protect_data['name'] = str(meta).replace("HTTP_X_P_G_", "")
            protect_data['code'] = request.META[meta]
            break
    
    if not protect_data:
        return False
    
    if not validate_hash(protect_data):
        return False
    
    comment.headers_data = str(request.META)