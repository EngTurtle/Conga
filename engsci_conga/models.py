__author__ = 'Oliver'

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import datetime
from settings import MEDIA_URL

class Course(models.Model):
    year = models.SmallIntegerField(verbose_name = 'Course Year')
    course_code = models.CharField(verbose_name = 'Course Code', max_length = 7, primary_key = True)
    course_name = models.CharField(verbose_name = 'Course Name', max_length = 50)

    def __unicode__(self):
        return self.course_code

    def get_absolute_url(self):
        """
        returns the url of this course.
        """
        return reverse('engsci_conga.views.courses_view', kwargs = {'course': self.course_code})


class File_type(models.Model):
    """This represents the types of files on the site"""
    type_name = models.CharField(max_length = 50)
    type_weighting = models.SmallIntegerField(unique = True)

    def __unicode__(self):
        return self.type_name


class Student_file(models.Model):
    course = models.ForeignKey(Course)
    owner = models.ForeignKey(User)
    note = models.FileField(upload_to = 'userfile/{date_time}'.format(
        date_time = str(datetime.now()).split(".")[0].replace(':', '_').replace('-', '_').replace(' ', '/'))
    )
    last_modified = models.DateTimeField(auto_now = True, editable = False)
    name = models.CharField(max_length = 100, blank = True)
    file_type = models.ForeignKey(File_type)
    year = models.SmallIntegerField(verbose_name = 'Year of file')

    def __unicode__(self):
        return self.note.name

    def get_absolute_url(self):
        url = '/{media_file}{user}/{pk}/'.format(
            media_file = MEDIA_URL,
            user = self.owner.username,
            pk = self.pk
        )
        return url
