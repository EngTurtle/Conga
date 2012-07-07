__author__ = 'Oliver'

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('Doc_sharing.views',
                       url(r'^(?P<user>\w*)/(?P<pk>\d*)/$', 'file_download'),
                       url(r'^(?P<user>\w*)/(?P<pk>\d*)/delete/$', 'doc_delete'),
                       )