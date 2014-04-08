from django.utils import translation
import settings
from mobler.browscap import browser


class LocaleMiddleware(object):
    def process_request(self, request):
        if request.path[0:6] == '/admin':
            translation.activate('en-US')
        else:    
            language = translation.get_language_from_request(request)
            if language not in ('ru-RU', 'ru'):
                language = settings.LANGUAGE_CODE
            translation.activate(language)
            request.LANGUAGE_CODE = translation.get_language()

class MobileDetectionMiddleware(object):
    def process_request(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        is_mobile = browser.detect_mobile(user_agent)
        
        request.session['is_mobile'] = is_mobile

