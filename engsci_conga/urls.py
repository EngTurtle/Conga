__author__ = 'Oliver'

from django.conf.urls.defaults import patterns, include, url

urlpatternts = patterns('engsci_conga.views',
	url(r'^(?P<course>\d+)/$', include('engsci_conga.views.course_view')),

	)