from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Course(models.Model):
    year = models.SmallIntegerField(verbose_name = 'Course Year')
    course_code = models.CharField(verbose_name = 'Course Code', max_length = 7, primary_key = True)
    course_name = models.CharField(verbose_name = 'Course Name', max_length = 50)

    def __unicode__(self):
        return self.course_code

    def save(self, *args, **kwargs):
        # So the course code is always stored uppercase
        self.course_code = self.course_code.upper() # TODO move this to the clean function
        super(Course, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        returns the url of this course.
        """
        return reverse('engsci_conga.views.courses_view', kwargs = {'course': self.course_code})