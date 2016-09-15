from django.contrib.auth import views as auth_views
from django.conf.urls import  url

from .forms import LoginForm
from .views import (
    home,
    account_login,
    signup,
    )

urlpatterns = [
    # url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html',
    #     'authentication_form': LoginForm}, name="login"),
    url(r'^accounts/login/$', account_login, name="account_login"),
    url(r'^accounts/signup/$', signup, name="signup"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/accounts/login'}),
    url(r'^$', home, name="home"),

    ]
