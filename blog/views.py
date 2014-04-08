from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
from blog.models import Post
from tagging.models import Tag
from django.template.context import RequestContext
from blog.utils import get_protect_data

def get_tag_cloud():
    try:
        return Tag.objects.cloud_for_model(Post, 6, filters={'status':Post.STATUS_PUBLIC}, min_count=1)[:20]
    except:
        pass
    
    return []

def post_list(request):
    posts = []
    post_cloud = get_tag_cloud()
    
    try:
        posts = Post.objects.filter(status=Post.STATUS_PUBLIC).order_by('-created_at')
    except :
        pass
    return render(request, 'blog/post_list.html', {'posts': posts, 'post_cloud': post_cloud})

def post_list_by_tag(request, tag):
    post_cloud = get_tag_cloud()
    
    try:
        posts = Post.objects.filter(status=Post.STATUS_PUBLIC, tag__contains=tag).order_by('-created_at')
        for post in posts:
            post.tag = [item.lstrip().rstrip() for item in post.tag.split(",")]
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/post_list_by_tag.html', {'posts': posts, 'tag_search': tag, 'post_cloud': post_cloud})

def post_detail(request, slug = ''):
    post_cloud = get_tag_cloud()
    statistic_disable = False
    protect = get_protect_data()
        
    if(slug):
        try:
            post = Post.objects.get(slug=slug)
            if post.status is Post.STATUS_DRAFT:
                statistic_disable = True
        except Post.DoesNotExist:
            raise Http404
        
    return render(request, 'blog/post_detail.html', {'post': post, 'post_cloud': post_cloud, 'statistic_disable':statistic_disable, 'protect' : protect}, context_instance=RequestContext(request))

def tag_lookup(request):
    # Default return list
    results = []
    if request.method == "GET":
        if request.GET.has_key(u'q'):
            value = request.GET[u'q']
            # Ignore queries shorter than length 2
            if len(value) > 2:
               TI = Tag.objects.filter(name__istartswith=value.lower())
               results = [ x.name for x in TI]
    return HttpResponse('\n'.join(results), mimetype='text/plain')