"""tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import caloriewatcher.views
import userprofile.views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', caloriewatcher.views.home, name='home'),
    url(r'^diary/$', caloriewatcher.views.diary, name='diary'),
    url(r'^food-search/$', caloriewatcher.views.food_search, name='food_search'),
    url(r'^add_food/$', caloriewatcher.views.add_food, name='add_food'),
    url(r'^exercise-search/$', caloriewatcher.views.exc_search, name='exc_search'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login-Register/$', caloriewatcher.views.login, name='login'),
    url(r'^profile/$', userprofile.views.user_profile, name='user_profile'),


    # user auth urls
    url(r'^accounts/login/$', caloriewatcher.views.login, name='login'),
    url(r'^accounts/auth/$', caloriewatcher.views.auth_view, name='auth_view'),
    url(r'^accounts/logout/$', caloriewatcher.views.logout, name='logout'),
    url(r'^accounts/loggedin/$', caloriewatcher.views.loggedin, name='loggedin'),
    url(r'^accounts/invalid/$', caloriewatcher.views.invalid_login, name='invalid_login'),
    url(r'^accounts/register/$', caloriewatcher.views.register_user, name='register_user'),
    url(r'^accounts/register_success/$', caloriewatcher.views.register_success, name='register_success'),
    url(r'^accounts/profile/$', userprofile.views.user_profile, name='user_profile'),
    url(r'^accounts/profile_update/$', userprofile.views.profile_update, name='profile_update'),
]

if not settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()