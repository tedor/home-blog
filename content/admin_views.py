from django.shortcuts import render
from content.models import Picture
from django.middleware.csrf import get_token
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

def blog_list(request):
    if not request.user.is_superuser:        
        return HttpResponse("error")
    
    if request.POST and request.POST['object_id']:
        object_id = request.POST['object_id']
        try:
            images = Picture.objects.filter(type_id=object_id)
        except :
            pass
    
    return render(request, 'content/picture/list_blog.html', {'images':images, 
                                                                 'csrf_token':get_token(request), 
                                                                 'object_id':object_id
                                                                 })

def blog_uload(request):
    if not request.user.is_superuser:        
        return HttpResponse("error")
    
    if request.method == "POST" and request.is_ajax():
        filename = request.GET['qqfile']
        object_id = request.GET['object_id']
       
        image=SimpleUploadedFile(filename, request.raw_post_data, 'image/jpeg')
        p = Picture(caption=filename, type='blog', type_id=object_id, image=image)
        p.save() 
        return HttpResponse("ok")
    
    return HttpResponse("fail")
        
def blog_delete(request, item_id):
    if not request.user.is_superuser:        
        return HttpResponse("error")
    
    if request.method == "GET":
        try:
            p = Picture.objects.get(id=item_id)
            p.delete()
            return HttpResponse("ok")
        except ObjectDoesNotExist:
            pass
    
    return HttpResponse("fail")