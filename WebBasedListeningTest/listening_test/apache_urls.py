import os
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from listening_test.views import homepage, info_collection, question_ahead
from listening_test import views


static_dir = os.path.join(os.path.dirname(__file__), 'static').replace('\\','/')

urlpatterns = patterns('',
    (r'^listening_test/$', homepage),
    (r'^listening_test/info_collection$', info_collection),
    (r'^listening_test/question/plus/(0?[1-9]|[1-2][0-9])/$', question_ahead),
	url(r'listening_test/^login/$','listening_test.views.login'),
	url(r'listening_test/^register/$','listening_test.views.register'),
	url(r'listening_test/^logout/$','listening_test.views.logout'),
	url(r'listening_test/^mp3/$','listening_test.views.mp3'),
	url(r'listening_test/^answer/$','listening_test.views.answer'),
	url(r'listening_test/^back/$','listening_test.views.back'),
	url(r'listening_test/^admin/', include(admin.site.urls)),
	url(r'listening_test/^static/(?P<path>.*)$','django.views.static.serve', {'document_root': static_dir}),
)