import os
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from listening_test.views import homepage, info_collection, question_ahead
from listening_test import views


static_dir = os.path.join(os.path.dirname(__file__), 'static').replace('\\','/')

urlpatterns = patterns('',
    (r'^$', homepage),
    (r'^info_collection$', info_collection),
    (r'^question/plus/(0?[1-9]|[1-2][0-9])/$', question_ahead),
	url(r'^login/$','listening_test.views.login'),
	url(r'^register/$','listening_test.views.register'),
	url(r'^logout/$','listening_test.views.logout'),
	url(r'^mp3/$','listening_test.views.mp3'),
	url(r'^answer/$','listening_test.views.answer'),
	url(r'^back/$','listening_test.views.back'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^static/(?P<path>.*)$','django.views.static.serve', {'document_root': static_dir}),
)