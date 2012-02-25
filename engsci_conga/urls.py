__author__ = 'Oliver'

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('engsci_conga.views',
	url(r'^(?P<course>\w{3}\d{3,4})/$', 'coursesview'),

	)