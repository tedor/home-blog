from django.utils.safestring import mark_safe
from django import forms
from django.template import loader

class TextFieldWithPictures(forms.Textarea):  
    def render(self, name, value, attrs=None):
        s = super(TextFieldWithPictures, self).render(name, value, attrs)
        t = loader.render_to_string('content/picture/upload_blog.html')
        return mark_safe(s+t)