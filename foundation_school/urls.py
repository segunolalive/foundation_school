"""foundation_school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from rest_framework import routers

from authentication.api.views import AccountViewSet, ProfileViewSet
from authentication.forms import LoginForm
# from course.api

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
# router.register(r'profile', ProfileViewSet)
# router.register(r'course')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/fs/', include(router.urls)),
    url(r'^api/fs/course/', include("course.api.urls", namespace="course_api")),
    url(r'^course/', include("course.urls", namespace="course")),
    url(r'', include("authentication.urls", namespace="authentication")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
