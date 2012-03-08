__author__ = 'Oliver'

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('user_manage.views',
                       url(r'^register/$', 'register'),
                       )