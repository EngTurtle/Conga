__author__ = 'Oliver'

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import login

urlpatterns = patterns('user_manage.views',
                       url(r'^register/$', 'register'),
                       )

urlpatterns += patterns('',
                        url(r'^login/$', login),
                        #url(r'^logout/$', logout(template_name='registration/logout.html')),
)