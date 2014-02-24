import os
import sys

import django.core.handlers.wsgi
sys.path.append(r'C:/Python26/Lib/site-packages/django/bin/listening_test3.27')
os.environ['DJANGO_SETTINGS_MODULE'] = 'listening_test.apache_settings'
application = django.core.handlers.wsgi.WSGIHandler()

