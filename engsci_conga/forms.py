from Course_Manage.models import Course

__author__ = 'Oliver'

from django import forms
from models import  File_type
from datetime import date
from django.utils.translation import ugettext_lazy as _

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course


class File_upload(forms.Form):
    ALL_COURSES = Course.objects.all()
    FILE_TYPES = File_type.objects.all()

    course = forms.ModelChoiceField(queryset = ALL_COURSES,
                                    label = u'Course Code',
                                    empty_label = u'Please select an associated course')
    file_type = forms.ModelChoiceField(queryset = FILE_TYPES,
                                       label = u'File Type')
    note = forms.FileField(required = True,
                           label = u'File')
    name = forms.CharField(required = False,
                           label = u'File Name',
                           help_text = u'default to your filename')
    year = forms.IntegerField(label = 'Year',
                              initial = date.today().year)

    def clean_year(self):
        year = self.cleaned_data['year']
        current_year = int(str(date.today()).split('-')[0])

        if year < 1970 or year > current_year:
            raise forms.ValidationError(_("please enter a valid year"))
        return self.cleaned_data['year']

