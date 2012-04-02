from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from filetransfers.api import serve_file
from engsci_conga.models import Student_file
from django.http import Http404, HttpResponseRedirect
from django.dispatch import receiver
from django.db.models.signals import post_delete
import settings
import os

__author__ = 'Oliver'

def download_handler(request, user, pk):
    upload = get_object_or_404(Student_file, pk = pk)
    if upload.owner.username != user:
        raise Http404
    return serve_file(request, upload.note, save_as = True)


@csrf_protect
@login_required
def delete_handler(request, user, pk):
    error = None
    f = get_object_or_404(Student_file, pk = pk)

    if f.owner.username != user:
        raise Http404

    if f.owner != request.user:
        error = u"This is not your file! You are now on Santa's naughty list!!"
    elif request.method == 'POST' and f.owner == request.user:
        f.delete()
        return HttpResponseRedirect(reverse(
            'engsci_conga.views.courses_view',
            kwargs = {'course': str(f.course)}
        )
        )

    return render_to_response('delete_form.html', {'error': error, 'f': f},
                              context_instance = RequestContext(request))


@receiver(post_delete, sender = Student_file)
def file_delete(sender, instance = None, **kwargs):
    """
    This signal handler deletes the associated file from disk when a student file is deleted from the database.
    """
    if instance is not None:
        path = "{media_files}/{file_dir}".format(media_files = settings.MEDIA_ROOT,
                                                 file_dir = instance.note.name
        )

        # allow for Windows and UNIX environments.
        if path[0] != '/':
            path = path.replace('/', '\\')

        try:
            os.remove(path)
        except WindowsError:
            pass
        except OSError:
            pass

            # TODO add logging if there is an exception
    pass