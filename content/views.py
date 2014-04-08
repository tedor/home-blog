from django.shortcuts import render
from blog.models import Post
from content.models import MindStream
from django.contrib.markup.templatetags.markup import markdown
from django.template import loader, Context
from django.contrib.sites.models import Site

def get_mind_stream_random():
    try:
        item = MindStream.objects.order_by('?')[0]

        t = loader.get_template('content/get_mind_stream_random.html')
        c = Context({'item':item})
        return t.render(c)
    except :
        return ''

def home(request):
    data = get_all_data()
    
    ''' Get mind stream content '''
    data_random_content = get_mind_stream_random()

    return render(request, 'content/home.html', {'data':data, 'data_random_content':data_random_content})

def get_all_data():
    data = []
    try:
        ''' Get data from blog '''
        data = [{"title":v.title, "text":markdown(v.text.split(Post.TEXT_CUT)[0]), "date":v.created_at, "url":v.get_absolute_url()} for v in Post.objects.filter(status=Post.STATUS_PUBLIC).order_by('-created_at')[:10]]
    
        data.sort(key=lambda item: item['date'], reverse=True)
        data = data[:10]
    except :
        pass
    
    return data

def sort_data(data):
    result = []
    result.pop()
    return data

''' Static pages '''
def developers(request):
    return render(request, 'content/developers.html')

def about(request):
    return render(request, 'content/about.html')

def robots(request):
    current_site = Site.objects.get_current()
    return render(request, 'content/robots.txt', {'current_site':current_site}, mimetype='text/plain')
