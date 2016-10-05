from django.contrib.auth import views as auth_views
from django.conf.urls import  url

from .forms import LoginForm
from .views import (
    account_login,
    home,
    signup,
    profile_detail,
    update_profile,
    )

urlpatterns = [
    url(r'^accounts/login/$', account_login, name="account_login"),
    url(r'^accounts/signup/$', signup, name="signup"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/accounts/login'}),
    url(r'^accounts/update-profile/$', update_profile, name="update_profile"),
    url(r'^accounts/profile/$', profile_detail, name="profile_detail"),
    url(r'^$', home, name="home"),

    ]
