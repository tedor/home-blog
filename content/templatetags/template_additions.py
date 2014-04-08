from django import template
from django.conf import settings

register = template.Library()

@register.tag
def setting ( parser, token ): 
    try:
        tag_name, option = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents[0]
    return SettingNode( option )

class SettingNode ( template.Node ): 
    def __init__ ( self, option ): 
        self.option = option

    def render ( self, context ): 
        # if FAILURE then FAIL silently
        try:
            return str(settings.__getattr__(self.option))
        except:
            return ""

@register.tag
def analyticsjs(parser, token):
    return ShowAnalyticsJS()

class ShowAnalyticsJS(template.Node):
    def render(self, context):
        #if 'user' in context and context['user'] and context['user'].is_staff:
        #    return "<!-- Goggle Analytics not included because you are a staff user! -->"

        if settings.DEBUG:
            return "<!-- Goggle Analytics not included because you are in Debug mode! -->"

        return """
        <script type="text/javascript">var _gaq = _gaq || [];_gaq.push(['_setAccount', 'UA-29589044-1']);_gaq.push(['_trackPageview']);(function() {var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);})();</script>
        <div style="display:none;"><script type="text/javascript">(function(w, c) { (w[c] = w[c] || []).push(function() { try { w.yaCounter12919777 = new Ya.Metrika({id:12919777, enableAll: true}); } catch(e) { } }); })(window, "yandex_metrika_callbacks");</script></div><script src="//mc.yandex.ru/metrika/watch.js" type="text/javascript" defer="defer"></script><noscript><div><img src="//mc.yandex.ru/watch/12919777" style="position:absolute; left:-9999px;" alt="" /></div></noscript>    
        """