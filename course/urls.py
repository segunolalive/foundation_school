from django.conf.urls import url
from .views import (
	chapter_list,
	subchapter_list,
	subsection_list,
	detail,
	)


urlpatterns = [

	url(r'^chapter$', chapter_list, name='chapter_list'),
	url(r'^chapter/(?P<pk>[0-9]+)$', subchapter_list, name='subchapter_list'),
	url(r'^chapter/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/$', subsection_list, name='subsection_list'),
	url(r'^chapter/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/(?P<slug2>[\w-]+)/$', detail, name='detail'),
]
