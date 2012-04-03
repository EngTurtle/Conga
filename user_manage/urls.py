__author__ = 'Oliver'

from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from django.views.generic.simple import direct_to_template
from registration.views import activate
from registration.views import register
from user_manage.forms import RegistrationForm

urlpatterns = patterns('',
                       url(r'^activate/complete/$',
                           TemplateView.as_view(template_name = 'registration/activation_complete.html'),
                           name = 'registration_activation_complete'),
                       # Activation keys get matched by \w+ instead of the more specific
                       # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
                       # that way it can return a sensible "invalid key" message instead of a
                       # confusing 404.
                       url(r'^activate/(?P<activation_key>\w+)/$',
                           activate,
                               {'backend': 'registration.backends.default.DefaultBackend'},
                           name = 'registration_activate'),
                       url(r'^register/$',
                           register,
                               {'backend': 'registration.backends.default.DefaultBackend',
                                'form_class': RegistrationForm},
                           name = 'registration_register'),
                       url(r'^register/complete/$',
                           TemplateView.as_view(template_name = 'registration/registration_complete.html'),
                           name = 'registration_complete'),
                       url(r'^register/closed/$',
                           direct_to_template,
                               {'template': 'registration/registration_closed.html'},
                           name = 'registration_disallowed'),
                       url(r'', include('registration.auth_urls')),
                       )
