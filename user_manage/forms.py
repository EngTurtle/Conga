__author__ = 'Oliver'

from django import forms
from registration import forms as reg_forms
from django.utils.translation import ugettext_lazy as _

# From the registration forms:
# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = {'class': 'required'}


class RegistrationForm(reg_forms.RegistrationForm):
    student_number = forms.IntegerField(max_value = 999999999, min_value = 1,
                                        label = u"Student Number")
    email = forms.EmailField(widget = forms.TextInput(attrs = dict(attrs_dict,
                                                                   maxlength = 75)),
                             label = _("Email address"),
                             initial = u"@utoronto.ca")


class RegistrationEmailRestriction(reg_forms.RegistrationFormNoFreeEmail):
    allowed_domains = [u'utoronto.ca', u'ecf.utoronto.ca', u'toronto.edu']

    def clean_email(self):
        """
        Check the supplied email address against a list of known allowed
        email domains.
        """
        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain not in self.allowed_domains:
            raise forms.ValidationError(_("This service is only for University of Toronto students and staff."))
        return self.cleaned_data['email']