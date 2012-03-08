__author__ = 'Oliver'
from django import forms
from models import Course, File_type

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course


class File_upload(forms.Form):
    ALL_COURSES = Course.objects.all()
    FILE_TYPES = File_type.objects.all()

    course = forms.ModelChoiceField(queryset = ALL_COURSES,
                                    label = u'Course Code',
                                    empty_label = u'Please select an associated course')
    type = forms.ModelChoiceField(queryset = FILE_TYPES,
                                  label = u'File Type')
    file = forms.FileField(required = True,
                           label = u'File')
    name = forms.CharField(required = False,
                           label = u'File Name',
                           label = u'default to your filename')

    # TODO write a function that renames the uploaded files in a structured way to prevent blackboard's one filename problem