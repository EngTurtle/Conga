from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'Course_Manage.views.course_list', name = "root"),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       # Conga
                       url(r'^course/', include('Course_Manage.urls')),

                       # User management
                       url(r'^auth/', include('user_manage.urls')),

                       # file download handling
                       url(r'^document', include('Doc_sharing.urls')),
                       url(r'^upload/', 'Doc_sharing.views.file_upload')
)
