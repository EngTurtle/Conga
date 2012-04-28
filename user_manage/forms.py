__author__ = 'Oliver'

from django import forms
from registration import forms as reg_forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from models import Student

# From the registration forms:
# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = {'class': 'required'}

allowed_domains = [ u'utoronto.ca', u'ecf.utoronto.ca', u'toronto.edu', u'mail.utoronto.ca' ]

def is_student_number(number):
    """
    Checks if the supplied student number is a valid U of T number.
    """
    return 850000000 < number < 1500000000


class RegistrationForm(reg_forms.RegistrationForm):
    student_number = forms.IntegerField(max_value = 1500000000, min_value = 1,
                                        label = u"Student Number")
    email = forms.EmailField(widget = forms.TextInput(attrs = dict(attrs_dict,
                                                                   maxlength = 75)),
                             label = _("Email address"),
                             initial = u"@utoronto.ca"
    )


    def clean_email(self):
        """
        Check the supplied email address against a list of known allowed
        email domains.
        """
        email = self.cleaned_data[ 'email' ]

        if email.split('@')[ 1 ] not in allowed_domains:
            raise forms.ValidationError(_("This service is only for University of Toronto students and staff."))

        if User.objects.filter(email__iexact = email):
            raise forms.ValidationError(_("This email address has already been registered."))

        return self.cleaned_data[ 'email' ]

    def clean_student_number(self):
        """
        Checks if the supplied student number is a valid U of T number.
        """
        number = self.cleaned_data[ 'student_number' ]
        if not is_student_number(number):
            raise forms.ValidationError(_("Please enter a valid U of T student number."))
        if Student.objects.get(student_number = number):
            raise forms.ValidationError(_("This Student number has already been registered."))
        return self.cleaned_data[ 'student_number' ]
