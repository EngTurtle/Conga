from Course_Manage.models import Course

__author__ = 'Oliver'

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import datetime
from settings import MEDIA_URL
from django.dispatch import receiver
from django.db.models.signals import post_save


class Doc_type(models.Model):
    """This represents the types of files on the site"""
    name = models.CharField(max_length = 50)
    weighting = models.SmallIntegerField(unique = True)

    def __unicode__(self):
        return self.name


class Document(models.Model):
    course = models.ForeignKey(Course)
    owner = models.ForeignKey(User)
    note = models.FileField(upload_to = 'userfile/{date_time}'.format(
        date_time = str(datetime.now()).split(".")[ 0 ].replace(':', '_').replace('-', '_').replace(' ', '/'))
    )
    last_modified = models.DateTimeField(auto_now = True, editable = False)
    name = models.CharField(max_length = 100, blank = True)
    file_type = models.ForeignKey(Doc_type)
    year = models.SmallIntegerField(verbose_name = 'Year of file')

    def __unicode__(self):
        return self.note.name.rsplit('/')[ -1 ]

    def get_view_url(self):
        url = '/{media_file}{user}/{pk}/'.format(
            media_file = MEDIA_URL,
            user = self.owner.username,
            pk = self.pk
        )
        return url

    def get_absolute_url(self):
        return self.get_view_url()

    def delete_url(self):
        return reverse('Doc_sharing.File_handling.views.delete_handler',
                       kwargs = {'user': self.owner.username, 'pk': self.pk})
        # TODO refactor the note handling to separate models to allow for different types of documents
        # (such as uploaded files, url links, and text files)


@receiver(post_save, sender = Document)
def note_name_fill(sender, **kwargs):
    # TODO move this function to the model's clean function
    """
    This signal fills in the name of the student file with the filename if the name is empty
    """
    instance = kwargs.get('instance')
    if instance is not None:
        if instance.name == u'':
            filename = instance.note.name.rsplit('/')[ -1 ]
            instance.name = filename
            instance.save()
    pass
