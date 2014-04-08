from comment.forms import CommentFormCustom
from django.contrib.comments.signals import comment_was_posted,\
    comment_will_be_posted
from comment.signals import save_name_to_cookie, send_to_email, check_meta_data
from comment.models import ProtectComment

comment_was_posted.connect(send_to_email)
comment_will_be_posted.connect(check_meta_data)

def get_form():
    return CommentFormCustom

def get_model():
    return ProtectComment