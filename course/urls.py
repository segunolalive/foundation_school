from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^$', views.chapter_list, name='chapter_list'),
	url(r'^(?P<pk>[0-9]+)/$', views.subchapter_list, name='subchapter_list'),
	url(r'^(?P<slug>[\w-]+)/$', views.subsection_list, name='subsection_list'),
	url(r'^(?P<pk>[0-9]+)/detail/$', views.detail, name='detail'),
]
