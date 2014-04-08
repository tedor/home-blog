import os
import sys
import django.core.handlers.wsgi

DIR_PROJECT = os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) )
sys.path.append( DIR_PROJECT )

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler() 