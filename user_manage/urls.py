__author__ = 'Oliver'

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse

urlpatterns = patterns('user_manage.views',
    #url(r'^register/$', 'register'),
)

urlpatterns += patterns('',
    (r'^login/$', login),
                        url(r'^logout/$', logout, {'next_page': reverse('engsci_conga.views.home')}),
                        )