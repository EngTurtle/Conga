from exceptions import WindowsError, OSError
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from Course_Manage.models import Course
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from settings import MEDIA_URL

__author__ = 'Oliver'

class Doc_type(models.Model):
    """This represents the types of files on the site"""
    name = models.CharField(max_length = 50)
    weighting = models.SmallIntegerField(unique = True)

    def __unicode__(self):
        return self.name


class Course_document(models.Model):
    """
    This model contains the information for a document shared for one course

    The actual file/link handling is done by other models, which is linked to with generic
    relationships
    """

    # Course_document attributes
    name = models.CharField(max_length = 100, blank = True)

    course = models.ForeignKey(Course)
    owner = models.ForeignKey(User)

    year = models.SmallIntegerField(verbose_name = 'Year of file')
    last_modified = models.DateTimeField(auto_now = True, editable = False)

    type = models.ForeignKey(Doc_type)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    doc = generic.GenericForeignKey('content_type', 'object_id')
    # During save, this needs to be checked if the related item is a subclass of Document_base and is unique


    def __unicode__(self):
        return self.name

    def view_url(self):
        # TODO convert this to a reverse url lookup
        url = '/{media_file}{user}/{pk}/'.format(
            media_file = MEDIA_URL,
            user = self.owner.username,
            pk = self.pk
        )
        return url

    def download_url(self):
        try:
            return self.doc.path
        except AttributeError:
            # should create log entry and flag this database entry.
            return ""

    def get_absolute_url(self):
        return self.view_url()

    def delete_url(self):
        return reverse('Doc_sharing.File_handling.views.delete_handler',
                       kwargs = {'user': self.owner.username, 'pk': self.pk})


class Document_base(models.Model):
    name = models.CharField(max_length = 50, blank = True)
    owner = models.ForeignKey(User)
    upload_time = models.DateTimeField(auto_now_add = True, editable = False)

    # storage size in MB
    size = models.SmallIntegerField

    course_doc = generic.GenericRelation(Course_document)

    def path(self):
        """
        All models of this class should have this method that returns the url path to this document
        """
        return ""

    def name(self):
        """ A function to return the verbose name of this document """
        return ''

    class Meta:
        abstract = True


class Test_document(Document_base):
    text = models.TextField(blank = True)
    size = 200

    def path(self):
        return 'test/{name}'.format(name = self.name)


class File_document(Document_base):
    file = models.FileField
    # Have the clean function auto set the size field

    def path(self):
        return reverse('Doc_sharing.views.file_download', kwargs = {'user': self.owner.username,
                                                                    'pk': self.pk})

    def name(self):
        return self.file.name.rsplit('/')[ -1 ]


#@receiver(post_save, sender = Course_document)
#def note_name_fill(sender, **kwargs):
#    # TODO move this function to the model's clean function
#    """
#    This signal fills in the name of the student file with the filename if the name is empty
#    """
#    instance = kwargs.get('instance')
#    if instance is not None:
#        if instance.name == u'':
#            filename = instance.note.name.rsplit('/')[ -1 ]
#            instance.name = filename
#            instance.save()
#    pass


@receiver(post_delete, sender = File_document)
def file_delete(sender, instance = None, **kwargs):
    """
    This signal handler deletes the associated file from disk when a student file is deleted from the database.
    """
    if instance is not None:
        path = "{media_files}/{file_dir}".format(media_files = settings.MEDIA_ROOT,
                                                 file_dir = instance.file.name)

        # allow for Windows and UNIX environments.
        if path[ 0 ] != '/':
            path = path.replace('/', '\\')

        try:
            os.remove(path)
        except WindowsError:
            pass
        except OSError:
            pass

            # TODO add logging if there is an exception
    pass