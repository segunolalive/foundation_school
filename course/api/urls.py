from django.conf.urls import url
from django.contrib import admin

from .views import (
    ChapterDetailAPIView,
    ChapterListAPIView,
    )

urlpatterns = [
    url(r'^$', ChapterListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>[\w-]+)/$', ChapterDetailAPIView.as_view(), name='detail'),
]
