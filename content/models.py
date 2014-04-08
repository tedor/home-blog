from django.db import models
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from cStringIO import StringIO
import os

from django.utils.translation import ugettext_lazy as _
import settings
from django.utils import timezone

class MindStream(models.Model):
    text = models.TextField(_('Mind stream content'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.text
    
    def save(self):
        if not self.created_at:
            self.created_at = timezone.now()
            
        super(MindStream, self).save()
    
def get_image_path(instance, filename):
    return os.path.join('picture', instance.type, instance.type_id, filename)

class Picture(models.Model):
    CHOICE_TYPES = (('blog', _('Blog')),)
    
    THUMB_BIG_SIZE = (920, 920)
    THUMB_SIZE = (400, 400)
    SUPER_THUMB_SIZE = (150, 150)
    THUMB_QUALITY = 90
    THUMB_TYPE = 'jpeg' 

    caption = models.CharField(_('Caption'), max_length=100)
    type = models.CharField(_('Type'), max_length=100, choices=CHOICE_TYPES)
    type_id = models.IntegerField(editable=False, default=0)
    image = models.ImageField(upload_to=get_image_path)
    image_thumb = models.ImageField(upload_to=get_image_path, editable=False)
    image_big = models.ImageField(upload_to=get_image_path, editable=False)
    image_super_thumb = models.ImageField(upload_to=get_image_path, editable=False)

    class Admin:
        list_display = ('caption','image',)

    def __unicode__(self):
        return self.caption

    def save(self):
        if self.id != None:
            old_obj = Picture.objects.get(id=self.id)
            if old_obj.image.path != self.image.path:
                self.clear_images(old_obj)
                
        image_thumb = Image.open(self.image)
        
        image_thumb.thumbnail(Picture.THUMB_BIG_SIZE, Image.ANTIALIAS)
        temp_handle = StringIO()
        image_thumb.save(temp_handle, Picture.THUMB_TYPE, quality=Picture.THUMB_QUALITY)
        temp_handle.seek(0)

        bsuf = SimpleUploadedFile(os.path.split(self.image.name)[-1], temp_handle.read(), content_type='image/' + Picture.THUMB_TYPE)
        self.image_big.save(os.path.splitext(bsuf.name)[0] + '_big_thumb.' + Picture.THUMB_TYPE, bsuf, save=False)
        
        image_thumb.thumbnail(Picture.THUMB_SIZE, Image.ANTIALIAS)
        temp_handle = StringIO()
        image_thumb.save(temp_handle, Picture.THUMB_TYPE, quality=Picture.THUMB_QUALITY)
        temp_handle.seek(0)

        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1], temp_handle.read(), content_type='image/' + Picture.THUMB_TYPE)
        self.image_thumb.save(os.path.splitext(suf.name)[0] + '_thumb.' + Picture.THUMB_TYPE, suf, save=False)
        
        image_thumb.thumbnail(Picture.SUPER_THUMB_SIZE, Image.ANTIALIAS)
        temp_handle = StringIO()
        image_thumb.save(temp_handle, Picture.THUMB_TYPE, quality=Picture.THUMB_QUALITY)
        temp_handle.seek(0)

        ssuf = SimpleUploadedFile(os.path.split(self.image.name)[-1], temp_handle.read(), content_type='image/' + Picture.THUMB_TYPE)
        self.image_super_thumb.save(os.path.splitext(ssuf.name)[0] + '_super_thumb.' + Picture.THUMB_TYPE, ssuf, save=False)
                       
        super(Picture, self).save()

    def delete(self):
        self.clear_images()
        super(Picture, self).delete()

    def clear_images(self, obj=None):
        image_path = self.get_image_path(obj)
        image_big_path = self.get_image_big_path(obj)
        image_thum_path = self.get_image_thumb_path(obj)
        image_super_thum_path = self.get_image_super_thumb_path(obj)

        if image_path:
            os.remove(image_path)
            
        if image_big_path:
            os.remove(image_big_path)

        if image_thum_path:
            os.remove(image_thum_path)

        if image_super_thum_path:
            os.remove(image_super_thum_path)

    def get_image_thumb_path(self, obj=None):
        try:
            if obj:
                path  = obj.image_thumb.path
            else:
                path  = self.image_thumb.path
            if os.path.exists(path):
                return path
        except Exception:
            pass
        return False

    def get_image_super_thumb_path(self, obj=None):
        try:
            if obj:
                path  = obj.image_super_thumb.path
            else:
                path  = self.image_super_thumb.path
            if os.path.exists(path):
                return path
        except Exception:
            pass
        return False

    def get_image_path(self, obj=None):
        try:
            if obj:
                path  = obj.image.path
            else:
                path  = self.image.path
            if os.path.exists(path):
                return path
        except Exception:
            pass
        return False

    def get_image_big_path(self, obj=None):
        try:
            if obj:
                path  = obj.image_big.path
            else:
                path  = self.image_big.path
            if os.path.exists(path):
                return path
        except Exception:
            pass
        return False
    
    @property
    def absolute_image_url(self):
        return u'%s%s' % (settings.MEDIA_URL, self.image)
    
    def absolute_image_big_url(self):
        return u'%s%s' % (settings.MEDIA_URL, self.image_big)
    
    @property
    def absolute_image_thumb_url(self):
        return u'%s%s' % (settings.MEDIA_URL, self.image_thumb)
    
    @property
    def absolute_image_super_thumb_url(self):
        return u'%s%s' % (settings.MEDIA_URL, self.image_super_thumb)

        
    '''
    def save(self):
        for field in self._meta.fields:
            if field.name == 'image':
                field.upload_to = 'photos/%d' % self.id
        super(Photo, self).save()'''