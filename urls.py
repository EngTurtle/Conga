from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'engsci_conga.views.home', name = "root"),

                       # Examples:
                       # url(r'^$', 'testing.views.home', name='home'),
                       # url(r'^testing/', include('testing.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       # Conga
                       url(r'^course/', include('engsci_conga.urls')),

                       # User management
                       url(r'^register/', include('user_manage.urls'))
)
