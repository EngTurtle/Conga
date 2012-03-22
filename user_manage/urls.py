__author__ = 'Oliver'

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse

urlpatterns = patterns('',
    # url(r'^register/$', register, {form_class:RegistrationForm,
    #                             disallowed_url:reverse('engsci_conga.views.home'),
    #                             template_name: 'registration/registration_form.html',
    #                             success_url:reverse('engsci_conga.views.home')}),
)

urlpatterns += patterns('',
                        url(r'^login/$', login),
                        url(r'^logout/$', logout, dict(next_page = reverse('engsci_conga.views.home'))),
                        )