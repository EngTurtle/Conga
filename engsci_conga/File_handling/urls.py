__author__ = 'Oliver'

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('engsci_conga.File_handling.views',
                       url(r'^(?P<user>\w*)/(?P<pk>\d*)/$', 'download_handler'),
                       url(r'^(?P<user>\w*)/(?P<pk>\d*)/delete/$', 'delete_handler'),
                       )