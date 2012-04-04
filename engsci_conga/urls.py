__author__ = 'Oliver'

from django.conf.urls.defaults import patterns, url
from Course_Manage.views import list_all_courses

urlpatterns = patterns('engsci_conga.views',
                       url(r'^(?P<course>\w{3}\d{3,4})/$', 'courses_view'),
                       url(r'all.json', list_all_courses)
)