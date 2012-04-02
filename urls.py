from django.conf.urls.defaults import patterns, include, url
from settings import MEDIA_URL

# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'engsci_conga.views.course_list', name = "root"),

                       # Examples:
                       # url(r'^$', 'testing.views.course_list', name='course_list'),
                       # url(r'^testing/', include('testing.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       # Conga
                       url(r'^course/', include('engsci_conga.urls')),

                       # User management
                       url(r'^auth/', include('user_manage.urls')),

                       # file download handling
                       url(r'^{media_url}'.format(media_url = MEDIA_URL), include('engsci_conga.File_handling.urls')),
                       url(r'^upload/', 'engsci_conga.views.file_upload')
)
