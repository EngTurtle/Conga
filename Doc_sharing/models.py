from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
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
    # During save, this needs to be checked if the related item is a subclass of Document_vase


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


class Document_base(models.Model):
    name = models.CharField(max_length = 50, blank = True)
    owner = models.ForeignKey(User)
    upload_time = models.DateTimeField(auto_now = True)

    # storage size in MB
    size = models.SmallIntegerField

    def path(self):
        """
        All models of this class should have this method that returns the url path to this document
        """
        return ""

    class Meta:
        abstract = True


class Test_document(Document_base):
    text = models.CharField(max_length = 200, blank = True)
    size = 200

    def path(self):
        return 'test/{name}'.format(name = self.name)

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