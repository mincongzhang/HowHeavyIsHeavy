import os
import sys
import django.core.handlers.wsgi
sys.path.append(r'C:/Python26/Lib/site-packages/django/bin/listening_test3.19/listening_test')
os.environ['DJANGO_SETTINGS_MODULE'] = 'listening_test.settings'
application = django.core.handlers.wsgi.WSGIHandler()

